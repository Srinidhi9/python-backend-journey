import json
tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except:
        tasks = []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def add_task():
    task = input("Enter task: ").strip()
    if task == "":
        print("Task cannot be empty")
        return
    tasks.append(task)
    save_tasks()
    print("Task added")


def view_tasks():
    if not tasks:
        print("No tasks available")
        return

    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task():
    view_tasks()

    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks()
            print("Task deleted")
        else:
            print("Invalid number")
    except:
        print("Enter valid number")


# MAIN PROGRAM
load_tasks()

while True:
    print("\n--- Task Manager ---")
    print("1. Add")
    print("2. View")
    print("3. Delete")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option")
    