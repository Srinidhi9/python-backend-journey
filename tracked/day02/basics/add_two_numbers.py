num1 = int(input("enter first num:"))
num2 = int(input("enter second num:"))

result = num1 + num2

if result % 2 == 0:
    print(f"sum is: {result} (even)")
else:
    print(f"sum is: {result} (odd)")