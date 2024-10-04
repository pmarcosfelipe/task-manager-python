def create_task(tasks, name):
  task = {
    "name": name,
    "completed": False
  }

  tasks.append(task)
  print(f"Task {name} was successfully created...")
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
    break
  elif choose == "6":
    break

  print("Program finalized.")