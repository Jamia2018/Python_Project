# -------------------------------
# Task Management App
# -------------------------------

def task():

    # This list stores all the tasks.
    tasks = []

    print("===================================")
    print(" Welcome to Task Management App ")
    print("===================================")

    # Ask user how many tasks they want to enter.
    total_task = int(input("How many tasks do you want to add? : "))

    # Take all tasks from the user.
    for i in range(1, total_task + 1):

        task_name = input(f"Enter Task {i}: ")

        tasks.append(task_name)

    print("\nYour Current Tasks")
    print(tasks)

    # Infinite loop
    while True:

        print("\n----------- MENU -----------")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        operation = int(input("Choose an option: "))

        # ---------------- Add ----------------
        if operation == 1:

            add = input("Enter new task: ")

            tasks.append(add)

            print(f"'{add}' added successfully!")

        # ---------------- Update ----------------
        elif operation == 2:

            updated_val = input("Enter task name to update: ")

            if updated_val in tasks:

                up = input("Enter new task: ")

                index = tasks.index(updated_val)

                tasks[index] = up

                print("Task updated successfully!")

            else:

                print("Task not found!")

        # ---------------- Delete ----------------
        elif operation == 3:

            delete_task = input("Enter task to delete: ")

            if delete_task in tasks:

                tasks.remove(delete_task)

                print("Task deleted successfully!")

            else:

                print("Task not found!")

        # ---------------- View ----------------
        elif operation == 4:

            print("\nToday's Tasks")

            if len(tasks) == 0:

                print("No tasks available.")

            else:

                for i, t in enumerate(tasks, start=1):

                    print(f"{i}. {t}")

        # ---------------- Exit ----------------
        elif operation == 5:

            print("Thank you for using Task Management App.")

            break

        # ---------------- Invalid ----------------
        else:

            print("Invalid Choice!")


# Calling Function
task()