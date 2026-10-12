# To-do list, with error handling
tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(number, "-", task)


while True:
    print()
    print("1) Show tasks  2) Add task  3) Remove task  4) Quit")
    choice = input("Choose: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("New task: ")
        tasks.append(task)
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
        print("Removed:", removed)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, or 4.")