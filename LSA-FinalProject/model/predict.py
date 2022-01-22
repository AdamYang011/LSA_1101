import numpy as np
import librosa
import os

TOTAL_FRAME_COUNT = 16000
MFCC_COUNT = 40

train_audio_path = "./data"
labels=os.listdir(train_audio_path)

from keras.models import load_model

model = load_model('./ASR.h5')

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
    prob = model.predict(X_pred)
    return labels[np.argmax(prob)]

#testdata 放要讀的wav檔s
path = './testdata/' 
waves = os.listdir(path)
for wave in waves:
  print(predict(path+wave))
 