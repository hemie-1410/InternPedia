import tkinter as tk
from tkinter import messagebox


def add_task(): 
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning!", "You must enter a task.")


def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except:
        messagebox.showwarning("Warning!", "You must select a task.")


def load_tasks():
    try:
        tasks = []
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        listbox.delete(0, tk.END)
        for task in tasks:
            listbox.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showwarning("Warning!", "Tasks file not found.")
    except Exception as e:
        messagebox.showwarning("Warning!", "An error occurred: " + str(e))


def save_tasks():
    tasks = []
    for i in range(listbox.size()):
        tasks.append(listbox.get(i))
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        messagebox.showwarning("Warning!", "An error occurred: " + str(e))


root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox = tk.Listbox(frame_tasks, height=10, width=50)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame_tasks)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=50)
entry.pack()

button_add_task = tk.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tk.Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tk.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()
