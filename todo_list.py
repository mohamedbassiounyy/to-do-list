todo_list = []

while True:
    user_action = input("Enter a command (add, view, remove, exit): ").strip().lower()

    if(user_action == "add"):
      task =input("Enter a task: ").strip()
      todo_list.append(task)
      print("Task added")
    
    elif(user_action == "view"):
      if not todo_list:
         print("No tasks to display.")
      else:
         print("Your to-do list: ")
         for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

    
    elif user_action == "remove":
        if not todo_list:
            print("No tasks to remove.")
        else:
            print("Your to-do list:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            try:
                task_index = int(input("Enter the task number to remove: ").strip())
                if 1 <= task_index <= len(todo_list):
                    removed_task = todo_list.pop(task_index - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif(user_action == "exit"):
      break
    else:
      print("Invalid command. Please try again.")


