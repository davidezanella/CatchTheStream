from streamsite import streamSite
import requests

class vidtome(streamSite):
    def __init__(self):
        streamSite.__init__(self, "vidtome")

    def getStreamUrl(self, url):
        r = requests.get(url)
        if(r.status_code != 200):
            print("Error getting url")
            return

        op = self.returnFirstReGroup('<input type="hidden" name="op" value="(.*)">', r.text)
        code = self.returnFirstReGroup('<input type="hidden" name="code" value="(.*)">', r.text)
        hash = self.returnFirstReGroup('<input type="hidden" name="hash" value="(.*)">', r.text)
        
        site = self.returnFirstReGroup('<Form method="POST" action="(.*)">', r.text)
        
        site = "http://vidtome.stream/" + site        

        r = requests.post(site, data = {
                'op': op, 
                'code': code,
                'hash': hash
            }
        )

        js_code = self.returnFirstReGroup("\d,'(.*)'\.", r.text)
        elems = js_code.split('|')

        eval_fn = self.returnFirstReGroup("<script>eval(.*)\n<\/script>", r.text)

        url1_n = self.returnFirstReGroup("\/\/(\d+)-", eval_fn)
        url2 = self.returnFirstReGroup("-(\d+)\.", eval_fn)
        site_n = self.returnFirstReGroup("\.(\d+)\.", eval_fn)
        domain_n = self.returnFirstReGroup("\.(\d+)\:", eval_fn)
        port_n = self.returnFirstReGroup("\:(\d+)\/", eval_fn)
        suburl1_n = self.returnFirstReGroup("\:\d+\/(\d+)\/", eval_fn)
        suburl2_n = self.returnFirstReGroup("\:\d+\/\d+\/(\d+)\/", eval_fn)
        file_n = self.returnFirstReGroup("\/\d+\/(\d+)\.", eval_fn)

        port = elems[int(port_n)]
        suburl1 = elems[int(suburl1_n)]
        suburl2 = elems[int(suburl2_n)]

        url1 = elems[int(url1_n)]
        site = elems[int(site_n)]
        domain = elems[int(domain_n)]
        file_name = elems[int(file_n)]      

        if(url1 == ""):
            url1 = url1_n  

        streamUrl = "http://" + url1 + "-" + url2 + "." + site + "." + domain + ":" + port + "/" + suburl1 + "/" + suburl2 + "/" + file_name + ".mp4"

        return streamUrl

