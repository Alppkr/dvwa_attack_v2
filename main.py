from attacks.IRA import IRA,bruteForce,commandInjection
from attacks.RFI import RFI,fileInclusion,fileUpload

if __name__ == "__main__":
    payload = {
    'username': 'admin',
    'password': 'password',
    'Login': 'Login'
    }
    #bruteForce("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    #commandInjection("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    #IRA("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
    fileUpload("http://web-dvwa.example.com:30064/",'login.php',payload).startAttack()
