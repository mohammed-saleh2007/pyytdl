# Python YouTube Video Downloader

A script Helps you to download videos from YouTube just you need the url

# Featuers
 - you can choose Audio or Video
 - you can choose how output filw (ex: myHBDvideo.mp4)
 - you can choose Video Quality

# ToDO
* [x] make it GUI application
* [ ] add audio only selection
* [ ] make it works via argements and parametrs
* [x] build for windows and linux
* [ ] make it easy to run (add installer or pkgs type)
* [ ] make android version
* [ ] add abilty to make a defualt file name for video and path with saved configration file

# How To use?
## CLI
- clone the repo
```
git clone https://github.com/mohammed-saleh2007/pyytdl
cd pyytdl
```
- get python and pip (ex: on termux)
```
pkg update
pkg install -y python python-pip
```
- first, get pytube via pip
```
python -m pip install git+https://github.com/pytube/pytube
```

- run it by
```
python3 main.py
```

## GUI
- clone the repo
```
git clone https://github.com/mohammed-saleh2007/pyytdl
cd pyytdl
```
- get python and pip (ex: on Arch)
```
pacman -Syu pyside6 python-pip python-pytube python-pip python-requests
```
or via pip on windows
```
pip install -r requermints.txt
```
for up-to-date version of pytube:
```
python -m pip install git+https://github.com/pytube/pytube
```
sometimes pip version of pytube be outdated or not working 
- run the program:
```
python qtpyytdl.py
```

## you can also use precompiled version on releases page
you can find it [here](https://github.com/mohammed-saleh2007/pyytdl/releases/tag/stable)

