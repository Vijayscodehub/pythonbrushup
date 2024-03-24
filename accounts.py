class Account:
#    """Simple Account class with balance"""

    def __init__(self,name,balance):  #__init__to initialize the class
        self.name = name
        self.balance = balance
        print("Account created for" +self.name)
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            
    def withdrawal(self,amount):
        if 0<amount<= self.balance:
            self.balance -= amount
        else:
            print("You don't have enough balance")
            self.show_balance
            
    def show_balance(self):
        print("Balance is {}" .format(self.balance))
    
if __name__ == "__main__":
    tim = Account("Tim",0)
    tim.show_balance()
    tim.deposit(10000)
    tim.withdrawal(50000)
    tim.show_balance()
    tim.withdrawal(2000)
    
    