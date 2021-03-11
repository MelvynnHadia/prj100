class Atm(object):
    def __init__(self, crdNo, pin, balance, cashtake, cashtook):
        self.crdNo = crdNo
        self.pin = pin
        self.balance = balance
        self.cashtake = cashtake
        self.cashtook = cashtook

    def atmcrdNo(self, crdNo):
        self.crdNo = crdNo

    def atmPin(self, pin, crdNo):
        self.pin[crdNo] = pin
    
    def ballInq(self, balance):
        self.balance = balance

    def cashTake(self, cashtake):
        self.cashtake = cashtake
    
    def cashTook(self, cashtook, cashtake, balance):
        self.cashtook = cashtake - balance


1 = Atm(100001, 9999, 30000, 10000)

print(1(atmPin()))
        

    