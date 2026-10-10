# To-do list
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
        show_tasks()
        number = int(input("Number to remove: "))
        removed = tasks.pop(number - 1)
        print("Removed:", removed)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, or 4.")