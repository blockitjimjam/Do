from tkinter import IntVar, Tk
from tkinter.ttk import *

class TodoElement: 
    def __init__(self, root: Tk, task_name: str) -> None:
        self.task_name: str = task_name
        self.completed: IntVar = IntVar()
        self.completed_bool: bool = False
        self.label: Label = Label(root, text=task_name)
        self.label.grid(row=root.grid_size()[1], column=0, padx=5, pady=5)
        self.entry: Entry = Entry(root, width=30)
        self.entry.insert(0, "Add description...")
        self.entry.grid(row=root.grid_size()[1], column=0, padx=5, pady=5)
        self.checkbox: Checkbutton = Checkbutton(root, variable=self.completed)
        self.checkbox.grid(row=root.grid_size()[1] - 1, column=1, padx=1, pady=1) # causes UI glitch, pady and padx minimized for temporary solution
        self.delete_button: Button = Button(root, text="Delete", command=self.delete_task)
        self.delete_button.grid(row=root.grid_size()[1] - 1, column=2, padx=5, pady=5)

    def delete_task(self) -> None:
        self.label.grid_forget()
        self.entry.grid_forget()
        self.checkbox.grid_forget()
        self.delete_button.grid_forget()
        # TODO (Ironic, this is a todo app lol.) - add way to actually delete the object. probably will be external.
