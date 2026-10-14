# To-do list, saved to a file
TASKS_FILE = "tasks.txt"


def load_tasks():
    loaded = []
    try:
        with open(TASKS_FILE) as file:
            for line in file:
                task = line.strip()
                if task != "":
                    loaded.append(task)
    except FileNotFoundError:
        pass
    return loaded


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(number, "-", task)


tasks = load_tasks()
print(f"Loaded {len(tasks)} task(s).")

while True:
    print()
    print("1) Show tasks  2) Add task  3) Remove task  4) Quit")
    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("New task: ").strip()
        if task == "":
            print("A task can't be blank.")
            continue
        tasks.append(task)
        save_tasks()
        print("Added:", task)
    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to remove.")
            continue
        show_tasks()
        try:
            number = int(input("Number to remove: "))
        except ValueError:
            print("Please enter a task number, like 1")
            continue
        if number < 1 or number > len(tasks):
            print(f"Pick a number from 1 to {len(tasks)}")
            continue
        removed = tasks.pop(number - 1)
        save_tasks()
        print("Removed:", removed)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, or 4.")