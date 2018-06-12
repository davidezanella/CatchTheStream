from streamsite import streamSite
import requests

class openload(streamSite):
    def __init__(self):
        streamSite.__init__(self, "openload")

    def getStreamUrl(self, url):
        r = requests.get(url)
        if(r.status_code != 200):
            print("Error getting url")
            return

        streamUrl = self.returnFirstReGroup('<video class="vjs-tech" id=".*" crossorigin="anonymous" poster=".*" src="(.*)"></video>', r.text)

        return streamUrl

