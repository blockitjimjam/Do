from tkinter import *
from tkinter.ttk import *
from todo.importance import Importance
from elements.todoTask import TodoElement

def add_task(app, name_entry: Entry) -> None: # app is an instance of App, from main.py. cicular imports cause problems here however, meaning I cannot annotate. I love python.
    app.tasks.append(TodoElement(app.instance, name_entry.get()))
