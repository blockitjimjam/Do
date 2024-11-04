from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.filedialog import *
from todo.importance import Importance
from todo.todo import Todo
from elements.todoTask import TodoElement
from tkinter.messagebox import showerror
import json

def add_task(app, name_entry: Entry) -> None: # app is an instance of App, from main.py. cicular imports cause problems here however, meaning I cannot annotate. I love python.
    if not name_entry.get() == "":
        app.tasks.append(Todo(Importance.LOW, name_entry.get(), "Add Description...", app.instance))
    else:
        showerror("Invalid Name", "Please write in the name of the task to continue.")

def save_task_config(app) -> None:
    with asksaveasfile(mode='w', defaultextension=".json", filetypes=[("Json files", "*.json"), ("Do files", "*.dotasks")]) as file:
        if file is not None:  
            save_data = {}
            for task in app.tasks:
                save_data[task.name] = task.desc
            json.dump(save_data, file, indent=4)
