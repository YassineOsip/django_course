class Account:
    
    def __init__(self,name,ndc,balance):
        self.name = name
        self.ndc = ndc
        self.balance = balance
    
    def deposit(self,amount): #deposer
        self.balance += amount
    
    def withdraw(self,amount): #retirer
        if self.balance <= 0:
            print("you dont have enough money sorry !")
        else:
            self.balance -= amount
    
    def show(self): # afficher la balance de compte
        print("your balance is " + str(self.balance) + "DH")
    
# Houssam Account
houssamAccount = Account("houssam","123654",100)
houssamAccount.show()
houssamAccount.withdraw(100)
houssamAccount.show()
houssamAccount.withdraw(100)

print("===============================")

# Mohamed Account
mohamedAccount = Account("mohamed","112435",1000)
mohamedAccount.show()
mohamedAccount.withdraw(100)
mohamedAccount.show()
mohamedAccount.withdraw(100)
mohamedAccount.show()