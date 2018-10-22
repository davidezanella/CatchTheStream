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

        codeUrl = self.returnFirstReGroup("\|http\|poster\|none\|preload\|.*\|(.*)\|sources\|Player\|new'\.split\('\|'\)\)\)", r.text)
        baseUrl = self.returnFirstReGroup("stream\|\|fastcdn\|(.*)\|data", r.text)

        streamUrl = "https://" + baseUrl + ".fastcdn.stream/" + codeUrl + "/v.mp4"

        return streamUrl

