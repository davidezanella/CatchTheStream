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

        js_code = self.returnFirstReGroup("\d,'(.*)'\.", r.text)
        elems = js_code.split('|')

        eval_fn = self.returnFirstReGroup("<script>eval(.*)\n<\/script>", r.text)

        url1_n = self.returnFirstReGroup("\/\/(\d+)", eval_fn)
        url2 = self.returnFirstReGroup("(\d+)\.", eval_fn)
        site_n = self.returnFirstReGroup("\.(\d+)\.", eval_fn)
        domain_n = self.returnFirstReGroup("\.(\d+)\:", eval_fn)
        port_n = self.returnFirstReGroup("\:(\d+)\/", eval_fn)
        suburl1_n = self.returnFirstReGroup("\:\d+\/(\d+)\/", eval_fn)
        suburl2_n = self.returnFirstReGroup("\:\d+\/\d+\/(\d+)\/", eval_fn)
        file_n = ord(self.returnFirstReGroup("\/([a-z])\.", eval_fn)) - 96 + 9

        port = elems[int(port_n)]
        suburl1 = elems[int(suburl1_n)]
        suburl2 = elems[int(suburl2_n)]

        url1 = elems[int(url1_n)]
        site = elems[int(site_n)]
        domain = elems[int(domain_n)]
        file_name = elems[int(file_n)]      

        if(url1 == ""):
            url1 = url1_n  
        
        first_part = url1 + "-" + url2
        if url1_n + "-" + url2 not in eval_fn:
            first_part = url1

        streamUrl = "http://" + first_part + "." + site + "." + domain + ":" + port + "/" + suburl1 + "/" + suburl2 + "/" + file_name + ".mp4"

        return streamUrl

