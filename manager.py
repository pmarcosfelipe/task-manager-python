def create_task(tasks, name):
  task = {
    "name": name,
    "completed": False
  }

  tasks.append(task)
  print(f"Task {name} was successfully created...")

  return

def show_tasks(tasks):
  print("\nTask List")
  for index, task in enumerate(tasks, start=1):
    status = "✓" if task["completed"] else " "
    name = task["name"]
    print(f"{index}. [{status}] {name}")
  return

def update_task_name(tasks, index_task, new_task_name):
  adjusted_index_task = int(index_task) - 1
  if adjusted_index_task >= 0 and adjusted_index_task < len(tasks):
    tasks[adjusted_index_task]["name"] = new_task_name
    print(f"Task {index_task} update to {new_task_name}")
  else:
    print(f"Task index {index_task} is invalid!")

  return

def complete_task(tasks, index_task):
  adjusted_index_task = int(index_task) - 1
  if adjusted_index_task >= 0 and adjusted_index_task < len(tasks):
    tasks[adjusted_index_task]["completed"] = True
    print(f"Task {index_task} completed!")
  else:
    print(f"Task index {index_task} is invalid!")
  return


tasks = [];
while True:
  print("\nMenu Task Manager: ")
  print("1. Create Task")
  print("2. Show Tasks")
  print("3. Update Task")
  print("4. Complete Task")
  print("5. Delete Complete Task")
  print("6. Quit")

  choose = input("Choose an option: ")

  if choose == "1":
    task_name = input("Type task name: ")
    create_task(tasks, task_name)
  elif choose == "2":
    show_tasks(tasks)
  elif choose == "3":
    show_tasks(tasks)

    index_task = input("Type the task number to update: ")
    new_task_name = input("Type the task name: ")

    update_task_name(tasks, index_task, new_task_name)
  elif choose == "4":
    

    index_task = input("Type the task number to complete: ")

    complete_task(tasks, index_task)
    show_tasks(tasks)
    break
  elif choose == "6":
    break

print("Program finalized.")