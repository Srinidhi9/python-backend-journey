balance = 1000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")