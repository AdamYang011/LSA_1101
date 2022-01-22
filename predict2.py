import numpy as np
import librosa
import os
import tflite_runtime.interpreter as tflite



TOTAL_FRAME_COUNT = 16000
MFCC_COUNT = 40

train_audio_path = "./data"
labels=['right','left']

def predict(file_path):
    samples, sr = librosa.load(file_path, sr=None, res_type='kaiser_fast')

    if len(samples) < TOTAL_FRAME_COUNT / 2 :
      return "none"
     # 右邊補 0
    if len(samples) < TOTAL_FRAME_COUNT : 
        samples = np.pad(samples,(0, TOTAL_FRAME_COUNT-len(samples)),'constant')
    elif len(samples) > TOTAL_FRAME_COUNT : 
        # 取中間一段
        oversize = len(samples) - TOTAL_FRAME_COUNT
        
        samples = samples[int(oversize/2):int(oversize/2)+TOTAL_FRAME_COUNT]

    # 驗證 mfcc 是否需要標準化
    mfcc = librosa.feature.mfcc(y=samples, sr=sr, n_mfcc=MFCC_COUNT)
    X_pred = mfcc.reshape(1, *mfcc.shape, 1)
    # 預測
  
    interpreter = tflite.Interpreter('float.tflite')
    interpreter.allocate_tensors()
    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test model on random input data.
    input_shape = input_details[0]['shape']
    x_pred = X_pred.astype(np.float32)
    interpreter.set_tensor(input_details[0]['index'], X_pred)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return labels[np.argmax(output_data)]


 