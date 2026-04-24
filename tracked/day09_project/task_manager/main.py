tasks = []

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("/n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print(tasks)

    elif choice == "3":
        task = input("Enter task to delete: ")
        
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found")

    elif choice == "4":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

        print("Tasks saved. Exiting...")
        break

    else:
        print("Invalid option")
    