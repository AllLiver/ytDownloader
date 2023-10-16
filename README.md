# ytDownloader
A simple and easy to use youtube video downloader with a graphical user interface!
# How to use
- First you need to download the program (instructions below)
- You then need to run the .exe (from the file menu) or .py (from your favorite IDE)\nThen put in a playlist or video link
- After launching it choose whatever file type you want it to be
- If you would like it to be a video, then select the video quality you want (low is lowest possible quality stream, medium is the middle possible quality stream, etc. Currently, it only downloads up to 720p progressive streams)
- If you would like to, set the download path you would like everything to be downloaded to
- Finally, hit download and it will get to work
# Downloading
If you are on Windows, go to the latest release and download the .exe from releases\
If you are on Mac or Linux download the latest .py from releases and then run these commands in some sort of command prompt:
```
pip install pytube pysimplegui
```
After that, run the .py file with an IDE or some other way to run .py's\
From my limited testing the .exe should be able to run on linux with wine installed\
Also, Mac and Linux users can build their own binary from source, instructions below
# How to build binary from source
If you would like to build your own binary (for the OS you are on) from source you need to
- Clone the repository
- Install all needed packages for building:
```
pip instal pytube pysimplegui pyinstaller
```
- Then run build.py
- If everything goes right, you should be able to launch the binary in the dist folder
# Disclaimer
I am not responsible for any copyright or terms of service infractions, and by using this it is assumed you have full permission to.
