from elements.element import Element
from tkinter import IntVar, Tk
from elements.element import Element
from tkinter.ttk import *

class TodoElement(Element): 
    def __init__(self, root: Tk, task_name: str, desc: str) -> None:
        self.task_name: str = task_name
        self.completed: IntVar = IntVar()
        self.label: Label = Label(root, text=task_name)
        self.label.grid(row=root.grid_size()[1], column=0, padx=5, pady=5)
        self.entry: Entry = Entry(root, width=30)
        self.entry.insert(0, desc)
        self.entry.grid(row=root.grid_size()[1], column=0, padx=5, pady=5)
        self.checkbox: Checkbutton = Checkbutton(root, variable=self.completed)
        self.checkbox.grid(row=root.grid_size()[1] - 1, column=1, padx=1, pady=1) # causes UI glitch, pady and padx minimized for temporary solution
        self.delete_button: Button = Button(root, text="Delete", command=self.delete_element)
        self.delete_button.grid(row=root.grid_size()[1] - 1, column=2, padx=5, pady=5)

    def delete_element(self) -> None:
        self.label.grid_forget()
        self.entry.grid_forget()
        self.checkbox.grid_forget()
        self.delete_button.grid_forget()
        # TODO (Ironic, this is a todo app lol.) - add way to actually delete the object. probably will be external.
