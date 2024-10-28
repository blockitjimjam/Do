from tkinter import *
from tkinter.ttk import *
from todo.importance import Importance
from elements.todoTask import TodoTask

def add_task(app, name: str):
    app.tasks.append(TodoTask(app.instance, name))
