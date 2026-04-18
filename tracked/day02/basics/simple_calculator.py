def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"


num1 = float(input("First number: "))
operator = input("Operator (+, -, *, /): ")
num2 = float(input("Second number: "))

result = calculate(num1, operator, num2)
print("Result:", result)