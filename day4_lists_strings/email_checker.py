email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid format")
else:
    print("Invalid format")