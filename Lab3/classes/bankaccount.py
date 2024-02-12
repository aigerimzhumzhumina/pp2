class Account:
    def __init__(self, owner , balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount, balance=0):
        self.balance += amount 
        print(f"The balance of {self.owner} is replenished for {amount} dollars (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount 
            print(f"Transferred {amount} dollars from {self.owner}'s account (¬‿¬ )")
        else:
            print("Insufficient funds ╥﹏╥")
owner = Bank_account("Nanami Kento")
owner.deposit(1000)
owner.withdraw(300)
owner.withdraw(5000)

        
    