def count_errors():
    try:
        with open("app.log", "r") as file:
            count = 0
            for line in file:
                if "ERROR" in line:
                    count += 1
            print("Total ERROR entries:", count)
    except FileNotFoundError:
        print("Log file not found.")

count_errors()