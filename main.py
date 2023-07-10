from attacks.IRA import IRA,bruteForce,commandInjection
from attacks.RFI import RFI,fileInclusion,fileUpload
from attacks.SQLInjection import sqlInjection,sqlInjectionBasic,sqlInjectionBlind
from attacks.XSS import xssDOM,xssReflect,xssStored,XSS
from utilities.report import report
import os

if __name__ == "__main__":
    payload = {
    'username': 'admin',
    'password': 'password',
    'Login': 'Login'
    }
    URL = os.getenv("DVWA_URL")
    IRA(URL,'login.php',payload).startAttack()
    RFI(URL,'login.php',payload).startAttack()
    sqlInjection(URL,'login.php',payload).startAttack()
    XSS(URL,'login.php',payload).startAttack()
    report.printAll()
    