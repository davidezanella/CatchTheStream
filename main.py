import subprocess
import os
import platform

from nowvideo import nowVideo
from speedvideo import speedVideo
from wstream import wStream
from turbovid import turboVid
from vidtome import vidtome

from openload import openload

if platform.system() == "Windows":
    vlc_dir = r"C:\Program Files (x86)\VideoLAN\VLC"
    assert os.path.isdir(vlc_dir)
    os.chdir(vlc_dir)

    vlc_cmd = "vlc.exe"
else: #maybe linux
    vlc_cmd = "vlc"


url = input('Paste the link of the video that you want to see:\n')

if "nowvideo" in url:
    site = nowVideo()
elif "speedvideo" in url:
    site = speedVideo()
elif "wstream" in url:
    site = wStream()
elif "turbovid" in url:
    site = turboVid()
elif "vidtome" in url:
    site = vidtome()
elif "oload" in url:
    site = openload()

else:
    print("Link type not recognised or not supported!!")
    exit(0)


print("Treating it as a ", site.siteName, " link...")


#stream = site.getStreamUrl("http://nowvideo.club/video/o8da8onvqd3w")

#stream = site.getStreamUrl("https://speedvideo.net/embed-5cn7a578qmgz.html")

stream = site.getStreamUrl(url)
subprocess.Popen([vlc_cmd, stream, "--quiet"])
