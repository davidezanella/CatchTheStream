from streamsite import streamSite
import requests

class wStream(streamSite):
    def __init__(self):
        streamSite.__init__(self, "wstream")

    def getStreamUrl(self, url):
        r = requests.get(url)
        if(r.status_code != 200):
            print("Error getting url")
            return

        codeUrl = self.returnFirstReGroup("\|http\|poster\|metadata\|preload\|.*\|(.*)\|sources\|Player\|new'\.split\('\|'\)\)\)", r.text)

        streamUrl = "https://blue.wstream.video/" + codeUrl + "/v.mp4"

        return streamUrl

