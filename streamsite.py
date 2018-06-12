import re

class streamSite():
    def __init__(self, siteName):
        self.siteName = siteName
    
    def getStreamUrl(self, url):
        return

    def returnFirstReGroup(self, pattern, text):
        m = re.search(pattern, text)
        return m.group(1)
