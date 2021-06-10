class user():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_details(self):
        print('-------customer_Details--------------')
        print("Name :",self.name)
        print("age :",self.age)
        print("Gender :",self.gender)
class Bank(user):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.amount + self.balance
        print("Account Balance has been updated",self.balance)
    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.balance):
            print('Insufficient Funds | Avialabla Balance is :',self.balance)
        else:
            self.balance = self.amount - self.balance
            print('Avilable balance has been updated :',self.balance)
    def view_balance(self):
        self.show_details()
        print("Final Account Balance is :",self.balance)
        
        
        
