from streamsite import streamSite
import requests

class speedVideo(streamSite):
    def __init__(self):
        streamSite.__init__(self, "speedvideo")

    def getStreamUrl(self, url):
        r = requests.get(url)
        if(r.status_code != 200):
            print("Error getting url")
            return

        streamUrl = self.returnFirstReGroup('var linkfile ="(.*)";', r.text)

        return streamUrl

