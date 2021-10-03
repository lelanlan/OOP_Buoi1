#Thay đổi các thuộc tính account_number, account_name, balance trong class BankAccount thành thuộc tính ẩn, và triển khai thêm các phương thức:
#get_account_number()
##get_balance()
#set_balance() - balance phải lớn hơn hoặc bằng 0
#Thay đổi các phương thức display(), withdraw() và deposit() sử dụng các phương thức getter và setter trên.
#Chú ý:
#Với withdraw(), amount phải lớn hơn 0 và nhỏ hơn balance
#Với deposit(), amount phải lớn hơn 0
#Nếu giá trị không phù hợp thì thông báo ra console

class BankAccount:
   def __init__(self,account_number, account_name,balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.set_balance=balance

   @property
   def get_account_number(self):
       return self.account_number

   @property
   def get_account_name(self):
       return self.account_name
   @property
   def get_account_balance(self):
       return self.balance
   @get_account_balance.setter
   def set_balance(self,balance):
       if balance>=0:
           self.balance=balance
       else:
           print("số dư tài khoản phải lớn hơn hoặc bằng 0")
   def withdraw(self,amount):
       if amount>0 and amount<self.get_account_balance:
           self.set_balance=self.get_account_balance-amount
       else:
           print("amount nhập vào không hợp lệ")
   def deposit(self,amount):
       if amount>0:
           self.set_balance=self.get_account_balance+amount
       else:
           print("amount nhập vào không hợp lệ")


bl=BankAccount("123","lan",9)
bl.withdraw(15)
bl.withdraw(5)
bl.withdraw(-1)
bl.deposit(10)
print(bl.__dict__)

