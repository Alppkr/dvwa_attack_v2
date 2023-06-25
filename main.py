from attacks.IRA import IRA,bruteForce,commandInjection
from attacks.RFI import RFI,fileInclusion,fileUpload
from attacks.SQLInjection import sqlInjection,sqlInjectionBasic,sqlInjectionBlind
from attacks.XSS import xssDOM,xssReflect,xssStored,XSS
from utilities.report import report

if __name__ == "__main__":
    payload = {
    'username': 'admin',
    'password': 'password',
    'Login': 'Login'
    }
    #bruteForce("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    #commandInjection("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    IRA("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    RFI("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    sqlInjection("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    XSS("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    report.printAll()
    