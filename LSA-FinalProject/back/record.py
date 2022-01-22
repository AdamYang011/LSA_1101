import pyaudio
import sys
from array import array
from sys import byteorder
import wave
import predict2
import audioop

def rec():
    

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000 #44100

    # 錄音長度
    RECORD_SECONDS = 1.4

    if len(sys.argv) < 2:
        file_path = './testdata/demo.wav'
    else:
        file_path = sys.argv[1]

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS, 
                    rate=RATE, 
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    # sample_width: 2 ==> 16 bits, 1 ==> 8 bits
    sample_width = p.get_sample_size(FORMAT)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    print ("start recording")

    # https://docs.python.org/zh-tw/3/library/array.html
    # signed short
    data_all=[]
    command = False
    for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        #print(type(data))
        #print(len(data))
        wf.writeframes(data)
        rms = audioop.rms(data, 2) / 32767
        if rms > 0.005 :
            #print(rms)
            command = True
        data_all += data_all
    print ("end recording")
    if command:
        return predict2.predict(file_path)
    else:
        return 'none'
    