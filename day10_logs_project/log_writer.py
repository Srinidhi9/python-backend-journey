from datetime import datetime

def write_log(level, message):
    with open("app.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {level} - {message}\n"
        file.write(log_entry)

print("1. INFO")
print("2. ERROR")

choice = input("Select log type: ")
message = input("Enter log message: ")

if choice == "1":
    write_log("INFO", message)
elif choice == "2":
    write_log("ERROR", message)
else:
    print("Invalid choice")

print("Log written successfully.")