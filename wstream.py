from streamsite import streamSite
import requests
import js2py


headers = {
    'User-Agent': 'My User Agent 1.0',
}

class wStream(streamSite):
    def __init__(self):
        streamSite.__init__(self, "wstream")

    def getStreamUrl(self, url):
        r = requests.get(url, headers=headers)
        if(r.status_code != 200):
            print("Error getting url", r.status_code)
            return


        js_code = self.returnFirstReGroup("eval\((.*)\)", r.text)
        
        f = js2py.eval_js("function() {hola_player=function(a){return a.file;}; return eval(" + js_code + ");}")

        streamUrl = f()
        
        return streamUrl

