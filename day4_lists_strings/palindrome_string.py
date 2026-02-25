text = input("Enter string: ")

reversed_text = text[::-1]

if text == reversed_text:
    print("Palindrome")
else:
    print("Not Palindrome")