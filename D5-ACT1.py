import os 
os.system('cls')

def remove_last_task():
    print("Current tasks:", tasks)
    print("Removing the last task:", tasks[-1])
    tasks.pop(-1)
    print("Updated tasks:", tasks)

def remove_first_task():
    print("Current tasks:", tasks)
    print("Removing the first task:", tasks[0])
    tasks.pop(0)
    print("Updated tasks:", tasks)

tasks = []

for _ in range(5):
    task = input("Enter a task: ")
    tasks.append(task)

print("Initial task list: ", tasks)

for _ in range(len(tasks)):
    task_status = input("Do you want to remove a task? (last/first): ").lower()

    if task_status == "last":
        remove_last_task()
    elif task_status == "first":
        remove_first_task()
    else:
        print("Invalid option")

print("Final task list: ", tasks)
