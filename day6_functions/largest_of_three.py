def find_largest(a, b, c):
    return max(a, b, c)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

largest = find_largest(n1, n2, n3)

print("Largest number is:", largest)