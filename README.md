聲控遊戲 
===========

概念發想
-----
雷霆戰機是我們的童年回憶，透過方向鍵翱翔中銀河之中，刺激好玩的遊戲過程，更是讓我們度過愉快的遊戲時光。近年來，機器學習是當紅科技，我們打算挑戰自我，嘗試將新科技結合在遊戲上，提供更為豐富的遊戲體驗。因此我們結合機器學習，訓練語音辨識模型，並透過口頭指令，操控戰機，提升遊戲刺激度與難度。

功能
-----
* 語音辨識
* 玩遊戲
* 喇叭輸出

使用設備
---------
* 樹梅派(pi4) *1
* 藍芽耳機  *1以上

安裝
--------
* ### 語音辨識Model
  *  llvmlite 
  *  librosa 
  *  Tensorflow lite
* ### 遊戲 : 雷霆戰機 
  * 遊戲介面 : pygame
 
* ### 實作過程筆記:
   * Notion: https://www.notion.so/Model-4b2a20e9577e4678ba091a12a37792d8
   
課堂中的應用
------
* SSH遠端連線
* Linux系統使用與實作

工作分配
-------
楊博丞:雷霆戰機遊戲製作、上台報告、Debug<br\>
張晉瑋:語音辨識模型訓練、整合語音辨識結果到遊戲中、Debug<br\>
黃姵馨:雷霆戰機遊戲介面製作、簡報製作、Debug<br\>
許雱茹:會議紀錄、Github資料整理、管理設備、Debug<br\>

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
