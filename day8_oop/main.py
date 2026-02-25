from student import Student
from bank_account import BankAccount
from user import User


# Student Test
s1 = Student("Srinidhi", 101, 88)
s1.display()
print("Passed:", s1.is_passed())

print("-" * 30)

# BankAccount Test
acc1 = BankAccount("Srinidhi", 10000)
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.show_balance()

print("-" * 30)

# User Test
user1 = User("srinidhi_dev", "sri@email.com")
user1.login()
user1.logout()