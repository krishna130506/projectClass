class Atm(object):
        def __init__(self,cardNumber,pin):
                self.cardNumber = cardNumber
                self.pin = pin

        def cashWithdrawal(self):
                print("cash withdrawed")

        def balanceEnquiry(self):
                print("your balance is 10000rs")

        
atm = Atm("1234567890", "1234")
print(atm.cashWithdrawal())
print(atm.balanceEnquiry())