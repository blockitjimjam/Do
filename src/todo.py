from tkinter import Tk
from todoTask import TodoElement
from importance import Importance
from todoTask import TodoElement
from tkinter import Tk
# not currently used but will be used later
class Todo:
    def __init__(self, importance: Importance, name: str, desc: str, root: Tk) -> None:
        self.importance: Importance = importance
        self.name: str = name
        self.desc: str = desc
        self.todoelement: TodoElement = TodoElement(root, name, desc)