聲控遊戲 
===========

概念發想
-----
有一陣子有一個極為流行的聲控遊戲-八分音符醬，透過判斷使用者的聲音大小去進行移動，以閃避障礙物的一個遊戲，看到聲控的遊戲能有如此不一樣的效果，因此我們打算也來自己實作一個透過聲音控制的小遊戲。
雷霆戰機與貪食蛇是我們的小時候極常接觸的兩個遊戲，讓我們度過許多愉快的遊戲時光，因此我們決定將這兩個遊戲加入聲控，期待能擦出不一樣的火花。

功能
-----
* 語音辨識
* 玩遊戲
* 喇叭輸出

使用設備
---------
* 樹梅派(pi4) *1
* 藍芽耳機  *1以上


語音指令辨識模型訓練
--------

參照mc6666大大的程式在colab上運行，成功得到語音辨識的model(訓練資料可以自己錄，或到kaggle尋找，但是要注意訓練資料與未來要辨識的語音指令需要是相同格式，不然極有可能失效)

參考: https://github.com/mc6666/DL_Book/blob/main/src/14_09_%E7%9F%AD%E6%8C%87%E4%BB%A4%E8%BE%A8%E8%AD%98.ipynb

可參考的錄音程式
https://github.com/mc6666/DL_Book/blob/main/src/14_10_record.py

為了要將model在樹梅派上運行所以必須安裝tensorflow lite，並且將model轉為tensorflow lite的格式

參考下方連結上將Keras model轉為 tflite檔
https://colab.research.google.com/github/tensorflow/examples/blob/master/lite/codelabs/digit_classifier/ml/step2_train_ml_model.ipynb?hl=zh-tw#scrollTo=AWROBI4iv9fY
https://www.tensorflow.org/lite/guide/get_started?hl=zh-cn

模型訓練就完成了


模組安裝
--------
* ### 錄音 : PyAudio
  * 在terminal輸入指令
  * sudo apt-get install portaudio.dev
  * sudo apt-get install python3-pyaudio
  * pip3 install wave
* ### 錄音 : 藍芽耳麥
  * 連上藍芽耳麥後 
  * 在terminal輸入指令
  * pactl load-module module-loopback latency_msec=1
* ### 使用.wav檔 : librosa
  * 在terminal輸入指令
  * LLVM_CONFIG=/usr/bin/llvm-config pip3 install llvmlite=0.31.0 numba==0.48.0 colorama==0.3.9 librosa==0.6.3
  * (numba跟numpy的版本需要留意，如果numpy發生錯誤建議先uninstall再安裝支援的版本)
* ### 運算模組 : tensorflow lite 
  * 在terminal輸入指令
  * pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime 
* ### 遊戲 : pygame 
  * 在terminal輸入指令
  * pip3 install pygame
* ### 實作過程筆記:
   * Notion: https://www.notion.so/Model-4b2a20e9577e4678ba091a12a37792d8

串接
--------
確認藍芽耳麥可以錄音後，透過tensorflow lite運行語音辨識的tflite檔案
將辨識結果當作命令傳到遊戲中，就完成了!!!

   
課堂中的應用
------
* SSH遠端連線
* Linux系統使用與實作

工作分配
-------
楊博丞：雷霆戰機遊戲製作、串接語音辨識與遊戲、上台報告、Debug<br/>
張晉瑋：語音辨識模型訓練與測試、整合語音辨識結果到遊戲中、Debug<br/>
黃姵馨：遊戲介面製作、貪食蛇遊戲製作、會議記錄、簡報製作、Debug<br/>
許雱茹：遊戲進入介面製作、會議紀錄、Github資料整理、管理設備、Debug<br/>

參考資料
-------
* ### 語音辨識 Model 參考資料 : 
   *  tensorflow 文本 https://www.tensorflow.org/lite/guide/python
   *  https://stackoverflow.com/questions/22479787/dpkg-need-an-action-option/36135513
   *  https://stackoverflow.com/questions/66092421/how-to-rebuild-tensorflow-with-the-compiler-flags
   *  https://www.notion.so/Model-4b2a20e9577e4678ba091a12a37792d8#aecfb2614da147afbe872844bc9452e1
   *  https://www.notion.so/Model-4b2a20e9577e4678ba091a12a37792d8#753c6534631b4df5979be89a6ce9c5a1
   *  kaggle-TensorFlow Speech Recognition Challenge : https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data 
* ### Raspberry pi4 操作參考資料:
   * 樹莓派（Raspberry Pi 4）開啟和連接藍牙https://blog.csdn.net/Cool2050/article/details/105615831
   *  樹莓派下安裝pyaudio與使用 https://www.twblogs.net/a/5b7cdbfd2b71770a43dce7c6
   *  how to hear mic sound over speakers- Ubuntu karmic https://superuser.com/questions/87571/how-to-hear-mic-sound-over-speakers-ubuntu-karmic
   *  https://www.footmark.info/embedded-systems/raspberry-pi/raspberry-pi-scrot-raspbian-desktop/
   *  在樹莓派4上安裝librosa，llvmlite的方向盤出現錯誤https://www.pythonheidong.com/blog/article/755228/4cd00cdd5bf7a46aba64/
   *  更新scipy:https://stackoverflow.com/questions/55252264/importerror-libf77blas-so-3-cannot-open-shared-object-file-no-such-file-or-di
   *  
