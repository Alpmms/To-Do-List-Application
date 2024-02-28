#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()

    def edit_task(self, task_index, new_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description
            self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                tasks_data = json.load(f)
            self.tasks = [Task(**task_data) for task_data in tasks_data]
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        command = input("Enter a command (add/mark/edit/delete/display/exit): ")
        if command == "add":
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif command == "mark":
            index = int(input("Enter the task index: "))
            todo_list.mark_completed(index)
        elif command == "edit":
            index = int(input("Enter the task index: "))
            description = input("Enter the new task description: ")
            todo_list.edit_task(index, description)
        elif command == "delete":
            index = int(input("Enter the task index: "))
            todo_list.delete_task(index)
        elif command == "display":
            todo_list.display_tasks()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


# In[ ]:




