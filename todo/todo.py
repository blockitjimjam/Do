from tkinter import Tk
from elements.todoTask import TodoElement
from todo.importance import Importance
from elements.todoTask import TodoElement
# not currently used but will be used later
class Todo:
    def __init__(self, importance: Importance, name: str, desc: str, root: Tk) -> None:
        self.importance: Importance = importance
        self.name: str = name
        self.desc: str = desc
        self.todoelement: TodoElement = TodoElement(root, name, desc)