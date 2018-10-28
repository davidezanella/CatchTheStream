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

        op = self.returnFirstReGroup('<input type="hidden" name="op" value="(.*)">', r.text)
        usr_login = self.returnFirstReGroup('<input type="hidden" name="usr_login" value="(.*)">', r.text)
        id = self.returnFirstReGroup('<input type="hidden" name="id" value="(.*)">', r.text)
        fname = self.returnFirstReGroup('<input type="hidden" name="fname" value="(.*)">', r.text)
        referer = self.returnFirstReGroup('<input type="hidden" name="referer" value="(.*)">', r.text)
        hash = self.returnFirstReGroup('<input type="hidden" name="hash" value="(.*)">', r.text)
        
        site = self.returnFirstReGroup('<Form method="POST" action=\'(.*)\'>', r.text)
        
        r = requests.post(site, data = {
                'op': op, 
                'usr_login': usr_login,
                'id': id,
                'fname': fname,
                'referer': referer,
                'hash': hash
            }
        )

        streamUrl = self.returnFirstReGroup('var linkfile ="(.*)";', r.text)

        return streamUrl

