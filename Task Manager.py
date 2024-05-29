
def add_task(tasks, task):
    tasks.append(task)

def remove_task(tasks, task_number):
    if 0 <= task_number < len(tasks):
        del tasks[task_number]
    else:
        print("Invalid number")


# This function shows the user the task next to the number it is ordered in
def show_tasks(tasks):
    print("Your tasks:")
    for i, task in enumerate(tasks):
        print(f"{i}. {task}")


# This is the main function that compiles everything together
def main():
    tasks = []
    while True:
        try:
            print("\nTo-do list:")
            print("1 - Add task")
            print("2 - Delete task")
            print("3 - Display tasks")
            print("4 - Quit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                task = input("Enter the task: ")
                add_task(tasks, task)
            elif choice == 2:
                task_number = int(input("Enter the number of the task to remove: "))
                remove_task(tasks, task_number)
            elif choice == 3:
                show_tasks(tasks)
            elif choice == 4:
                break
            else:
                print("Choice is not valid, please try again")
        except ValueError:
            print("Did you sneeze on your keyboard that wasn't even a whole number")


main()
