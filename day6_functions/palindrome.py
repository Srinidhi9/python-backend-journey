def is_palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return original == reverse


num = int(input("Enter number: "))

if is_palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")