def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


num = int(input("Enter number: "))
result = check_even_odd(num)

print(result)