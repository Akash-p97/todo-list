# To-Do List

tasks = [
    {"task": "Learn Python", "completed": True},
    {"task": "Practice SQL", "completed": True},
    {"task": "Learn GitHub", "completed": False}
]

def display_tasks(tasks):
    print("To-Do List:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(task["task"], "-", status)

def add_task(tasks, task_name):
    tasks.append({"task": task_name, "completed": False})

def complete_task(tasks, task_name):
    for task in tasks:
        if task["task"] == task_name:
            task["completed"] = True

def remove_task(tasks, task_name):
    for task in tasks:
        if task["task"] == task_name:
            tasks.remove(task)
            break

def pending_count(tasks):
    count = 0
    for task in tasks:
        if not task["completed"]:
            count += 1
    return count

display_tasks(tasks)
print("\nPending Tasks:", pending_count(tasks))
