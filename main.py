import os

# I'm going to start by creating an empty list of tasks
tasks = []
#A return screen because I hate typing this code everytime for each def
def ReturnScreen():
  print("Type 'y' to return.")
  input2 = input()
  if input2 == 'y':
    os.system('clear')
    Welcome_Page()
  else:
    print('Wrong input!')
    input4 = input("Please Type 'sorry' to restart: ")
    if input4 == 'sorry':
      ReturnScreen()
    else:
      ReturnScreen()
    

# Next I'm thinking of what features should I add to this "to do list"
# We will be adding Load, Save, Delete, Show, and Create function
def DeleteTask():
  print("Tasks:")
  for idx, task in enumerate(tasks, start=1):
        print(f"{idx}) {task}")
    
  if not tasks:
        print("No task to delete.")
        return
    
  input3 = int(input("Enter the number of the task you want to delete: ")) - 1

  if 0 <= input3 < len(tasks):
        del tasks[input3]
        print("Task deleted.")
  else:
        print("Invalid task number.")
    
  return ReturnScreen()

# THERE MAY BE SOME ISSUES WITH LOADING AND SAVING A FILE. I'll try to fix it
def LoadFile(file_path):
  with open(file_path, 'r') as file:
    tasks = file.readlines()
  return [task.strip() for task in tasks]

# THERE MAY BE SOME ISSUES WITH LOADING AND SAVING A FILE. I'll try to fix it
def SaveFile(file_path, tasks):
  with open(file_path, 'w') as file:
        file.write('\n'.join(tasks))
    

def Showtask():
  if not tasks:
    return 'There is no tasks.'
  else:
    return tasks
  return ReturnScreen()

def CreateTask():
  HowMany = int(input('How many tasks do you want to type in? '))
  n = HowMany
  for i in range(n):
    create = input('Enter your task: ')
    tasks.append(create)
  return ReturnScreen()

def Welcome_Page():
  print("Welcome to Your To Do List")
  print("\n")
  print("To get started, type cr to create, sh to show tasks, de to delete a certain task (Or l to load the tasks and s to save tasks to a file): ")
  user_input = input()
  
  if user_input == 'cr':
    CreateTask()
  elif user_input == 'sh':
    task_show = Showtask()
    if task_show:
          print("Tasks:")
          numb = 1
          for task in task_show:
              print(str(numb) +") " + task)
              numb += 1
    else:
        print("No tasks to show.")
    ReturnScreen()
  elif user_input == 'l':
    file_path = input('Enter file path: ')
    tasks = LoadFile(file_path)
    print("Task Loaded!")
    ReturnScreen()
  elif user_input == 's':
    file_path = input('Enter file path: ')
    SaveFile(file_path, tasks)
    print("Tasks saved!")
    ReturnScreen()
  elif user_input == 'de':
    DeleteTask()
  else:
        print("Invalid input.")

Welcome_Page()
  