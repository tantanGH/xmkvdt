# xmkvdt

Cross Platform VDT/V16 Data Builder

# INSTALL

1. Install ffmpeg

* [https://www.ffmpeg.org/](https://www.ffmpeg.org/)

2. Install git

* [https://gitforwindows.org/](https://gitforwindows.org/)

3. Install Python

* [https://www.python.org/](https://www.python.org/)

    pip install git+https://github.com/tantanGH/xmkvdt.git

or

    py -m pip install git+https://github.com/tantanGH/xmkvdt.git

# USAGE

例：MP4から30FPS/32.0kHz のV16を生成する。輝度ビットを使い65536色とする。PCMの音量を0.8倍とする。

    xmkvdt -fps 30 -ib -pv 0.8 hogehoge.mp4 hogehoge