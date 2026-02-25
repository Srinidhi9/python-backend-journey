def read_logs():
    try:
        with open("app.log", "r") as file:
            content = file.read()
            print("\n---- LOG FILE ----")
            print(content)
    except FileNotFoundError:
        print("Log file does not exist.")

read_logs()