from users import *

# user1 = User("sai","pass")
# print(user1.user_name)

class ATM:
    def __init__(self):
        self.users = []
        
    def register(self,user_name, password ):
        for users in self.users:
            if users.user_name.lower() == user_name:
                print(f'User already exists!')
                return 
        new_user = User(user_name, password)
        self.users.append(new_user)
    
    def isuser(self, user_name):
        for user in self.users:
            if user.user_name.lower() == user_name:
                return True
        return False


    def isPassWord(self,user_name,password):
        for user  in self.users:
            if user.user_name == user_name:
                return user.password == password
    
    def deposite(self,user,password,amount):
        if self.isuser(user) and self.isPassWord(user,password):
            for user in self.users:
                if user.user_name == user:
                    user.balance += amount
                    print(f"Amount {amount} is Credited")
                    return 
        else:
            print(f"Check the Username or password")

    def withdraw(self,user, password, amount):
        if self.isuser(user) and self.isPassWord(user,password):
            for users in self.users:
                if users.user_name == user:
                    if self.balance > amount:
                        self.balance -= amount
                        print(f"amount {amount} debited")
                        return         
        else:
            print(f"Check your username or password")

        
atm = ATM()
atm.register("sai", "1234")
atm.deposite("sai", "1234", "10_000")

        

    

            