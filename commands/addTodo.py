from tkinter import *
from tkinter.ttk import *
from todo.importance import Importance
from todo.todo import Todo
from elements.todoTask import TodoElement
from tkinter.messagebox import showerror

def add_task(app, name_entry: Entry) -> None: # app is an instance of App, from main.py. cicular imports cause problems here however, meaning I cannot annotate. I love python.
    if not name_entry.get() == "":
        app.tasks.append(Todo(Importance.LOW, name_entry.get(), "Add Description...", app.instance))
    else:
        showerror("Invalid Name", "Please write in the name of the task to continue.")
