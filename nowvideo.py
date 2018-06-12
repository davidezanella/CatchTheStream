from streamsite import streamSite
import requests

class nowVideo(streamSite):
    def __init__(self):
        streamSite.__init__(self, "nowvideo")

    def getStreamUrl(self, url):
        r = requests.get(url)
        if(r.status_code != 200):
            print("Error getting url")
            return

        op = self.returnFirstReGroup('<input type="hidden" name="op" value="(.*)">', r.text)
        code = self.returnFirstReGroup('<input type="hidden" name="code" value="(.*)">', r.text)
        hash = self.returnFirstReGroup('<input type="hidden" name="hash" value="(.*)">', r.text)
        
        site = self.returnFirstReGroup('<Form id="cty" method="POST" action="(.*)">', r.text)
        
        site = site.replace("..", "http://nowvideo.club")        

        r = requests.post(site, data = {
                'op': op, 
                'code': code,
                'hash': hash
            }
        )

        streamUrl = self.returnFirstReGroup('var player = new Clappr\.Player\({source: "(.*)",', r.text)

        return streamUrl

