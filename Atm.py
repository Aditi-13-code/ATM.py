class ATM (object):

    def __init__(self, name, card_number, pin_number, status):
        self.card_number = card_number
        self.pin_number = pin_number
        self.name = name
        self.status = status

    def start(self):
        print("started")

    def stop(self):
        print("stop")

    def cashWithdrawl(self):
        print("Cash Withdrawled")

    def BalanceEnquiry(self):
        print("Balanced Enquiry")

pin_code = ATM("Aditi-","1234567","7654321","Good")
pin_code1 = ATM("Aryan-","1234567","7654321","Bad")

print(pin_code.name)
print(pin_code.card_number)
print(pin_code.pin_number)
print(pin_code.status)
print(pin_code1.name)
print(pin_code1.card_number)
print(pin_code1.pin_number)
print(pin_code1.status)


    
