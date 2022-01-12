聲控遊戲 
===========
概念發想
-----
現如今早已是語音辨識的天下了，Apple有Siri、各廠家電也都紛紛加入AI語音辨識的功能、會議記錄的製作等等等，只需要用「說的」，就能讓機器替我們完成許多事，多方便啊!

因此我們想嘗試能不能用「說的」來玩遊戲，讓遊戲更加有趣，也發揮出語音辨識的優點。

功能
-----
* 語音辨識
* 玩遊戲
* 喇叭輸出

使用設備
-------
* 樹梅派(pi4) *1
* 麥克風  *1以上
* 喇叭 *1

安裝
--------
* ### Raspberry bluetooth connect
    * 1.查看藍芽開啟狀態 `systemctl status bluetooth`
    * 2.`sudo bluetoothctl`
        * a.`list`
        * b.`scan on` 掃描
        * c.`pair` your bluetooth device
        
* ### PyAudio
    * 1.`sudo apt-get install portaudio.dev`
    * 2.`sudo apt-get install python3-pyaudio`
* ### 錄音

* ### 下載
    * #### Tensorflow lite
        * 可以用來跑語音辨識的model
        * `pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime`
     * #### Librosa & llvmlite
         * 匯入聲音檔用的
         * 1.llvmlite
            * `pip install llvmlite` & `pip3 install librosa  
         * 2.librosa 
            *  `sudo apt install libblas-dev llvm python3-pip python3-scipy`
* ### Python3
  * #### pygame
  
 
課堂中的應用
------

工作分配
-------
參考資料
-------
* kaggle-TensorFlow Speech Recognition Challenge : https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data 
* 樹莓派（Raspberry Pi 4）開啟和連接藍牙https://blog.csdn.net/Cool2050/article/details/105615831
*  樹莓派下安裝pyaudio與使用 https://www.twblogs.net/a/5b7cdbfd2b71770a43dce7c6
*  how to hear mic sound over speakers- Ubuntu karmic https://superuser.com/questions/87571/how-to-hear-mic-sound-over-speakers-ubuntu-karmic
*  tensorflow 文本 https://www.tensorflow.org/lite/guide/python
*  
