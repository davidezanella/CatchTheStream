import subprocess
import os
import platform

from nowvideo import nowVideo

if platform.system() == "Windows":
    vlc_dir = r"C:\Program Files (x86)\VideoLAN\VLC"
    assert os.path.isdir(vlc_dir)
    os.chdir(vlc_dir)

    vlc_cmd = "vlc.exe"
else: #maybe linux
    vlc_cmd = "vlc"



site = nowVideo()
stream = site.getStreamUrl("http://nowvideo.club/video/o8da8onvqd3w")


subprocess.Popen([vlc_cmd, stream])
