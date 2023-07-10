from pydispatch import dispatcher
import utilities.report as report

class eventHandler():

    def __init__(self):
        pass

    def callback(self,event=None, signal=None,sender=None):
        if (signal == "Blocked"):
            report.report.blockedAttacked(sender)
        elif (signal == "Successful"):
            report.report.successfulAttacked(sender,event=event)
        elif (signal == "Response Time"):
            report.report.response(sender,event=event)
        print(event,signal,sender)
        
    def connect(self,listener,sender):
        dispatcher.connect(listener, sender=sender)
    def sendMessage(self,signal,sender,event):
        dispatcher.send(signal=signal, sender=sender, event=event)
    def disconnect(self,listener,sender):
         dispatcher.disconnect(listener, sender=sender)


