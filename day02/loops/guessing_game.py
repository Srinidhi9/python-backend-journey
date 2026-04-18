secret_number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct")
        break



secret_number = 7
attempts = 0
limit = 3

while attempts < limit:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct")
        break
else:
    print("You failed. The number was", secret_number)