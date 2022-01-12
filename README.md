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
Raspberry bluetooth connect:
    1.查看藍芽開啟狀態 `systemctl status bluetooth`
    2.`sudo bluetoothctl`
        a.`list`
        b.`scan on` 掃描
        c.`pair` your bluetooth device
    
* Python3
  * pygame
  * pyaudio
 
課堂中的應用
------

工作分配
-------
參考資料
-------
* kaggle-TensorFlow Speech Recognition Challenge : https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data 
* 樹莓派（Raspberry Pi 4）開啟和連接藍牙:https://blog.csdn.net/Cool2050/article/details/105615831
* 
