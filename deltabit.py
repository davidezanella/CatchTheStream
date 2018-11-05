from streamsite import streamSite
import requests
import time

class deltabit(streamSite):
    def __init__(self):
        streamSite.__init__(self, "deltabit")

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
        
        site = self.returnFirstReGroup("<Form method=\"POST\" action='(.*)'>", r.text)

        time.sleep(6)

        r = requests.post(site, data = {
                'op': op, 
                'id': id,
                'fname': fname,
                'hash': hash
            }
        )
        
        streamUrl = self.returnFirstReGroup('sources: \["(.*)"]', r.text)

        return streamUrl

