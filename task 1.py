def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your list.")

def remove_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
        return
    view_tasks(tasks)
    task_number = int(input("\nEnter the task number to remove: "))
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' has been removed from your list.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
