class User():
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        
    def show_user_data(self):
        print(f'your name : {self.name}')
        print(f'your age : {self.age}')
        print(f'your address : {self.address}')

class Bank(User):
    def __init__(self, name, age, address):
        super().__init__(name,age,address)
        self.balance = 0

    def deposite(self, amount):
        self.balance += amount
        print(f'you deposited : {amount}')        
        print(f'you balance after deposite : {self.balance}')        


    def withdraw(self, amount):
        if amount > self.balance:
            print(f'your poor and your balance : {self.balance}')
            return
        
        self.balance -= amount
        print(f'your withdrawed : {amount}')
        print(f'your balance after withdraw : {self.balance}')


    def show_details(self):
        self.show_user_data()
        print(f'balance : {self.balance}')




bank = Bank('omar', 22, 'negeer')
print(bank.deposite(1000))
print(bank.deposite(1000))
print(bank.withdraw(200))
print(bank.withdraw(2200))
print(bank.show_details())
