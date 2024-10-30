from tkinter import *
from tkinter.ttk import *
from todo.importance import Importance
from elements.todoTask import TodoElement

def add_task(app, name_entry: Entry): # app is an instance of App, from main.py. cicular imports cause problems here however, meaning i cannot annotate.
    app.tasks.append(TodoElement(app.instance, name_entry.get()))
