from pydispatch import dispatcher

class eventHandler():

    def __init__(self):
        pass

    def callback(self,event=None, signal=None,sender=None):
        print(event,signal,sender)
        
    def connect(self,listener,sender):
        dispatcher.connect(listener, sender=sender)
    def sendMessage(self,signal,sender,event):
        dispatcher.send(signal=signal, sender=sender, event=event)
    def disconnect(self,listener,sender):
         dispatcher.disconnect(listener, sender=sender)

if __name__ == "__main__":
        a = eventHandler()
        a.connect(a.callback,sender="alp")
        a.sendMessage(signal='information',sender="alp",event='attack started')
        a.sendMessage(signal='blocked',sender="alp",event='attack blocked')
        a.sendMessage(signal='successfull',sender="alp",event='attack success')
        a.sendMessage(signal='information',sender="alp",event='attacked stopped')


