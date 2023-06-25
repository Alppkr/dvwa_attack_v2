import requests
import re
import os
import urllib.parse
from pathlib import Path

class AttackSession:
    def __init__(self,host,authenticationPath,authPayload):
        self.host = host
        self.authenticationPath = authenticationPath
        self.authPayload= authPayload
    def authentication(self):
        with requests.Session() as s:
            url = self.host + self.authenticationPath
            try:
                r = s.get(url)
                if r.status_code != 200:
                    raise Exception("Website is not available")
            except:
                print("Can't reach the web site")
            try:
                authToken = re.search("user_token'\s*value='(.*?)'", r.text).group(1)
            except:
                print('Authentication Token could not find in web page')
            self.authPayload['user_token'] = authToken
            s.post(url, data=self.authPayload)
        return s
    
    def attack(self,s):
        pass
    def startAttack(self):
        self.attack(self.authentication())
            