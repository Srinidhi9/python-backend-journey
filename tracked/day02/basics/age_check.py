name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)

if age < 18:
    print("You are a minor")
else:
    print("You are an adult")

num1 = int(input("enter first num: "))
num2 = int(input("enter second num: "))

result = num1 + num2
print(f"sum is: {result}")