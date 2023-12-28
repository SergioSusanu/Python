class Payslip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            print(self.name + " is paid " + str(self.amount))
        else:
            print(self.name + " not paid yet")

John = Payslip("John","no",1000)
Ethan = Payslip("Ethan","yes",2000)

John.status()
Ethan.status()
John.pay()
John.status()