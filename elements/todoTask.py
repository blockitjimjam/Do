from tkinter import IntVar
from tkinter.ttk import *

class TodoTask:
    def __init__(self, root, task_name):
        self.task_name = task_name
        self.completed = IntVar()
        self.label = Label(root, text=task_name)
        self.label.grid(row=root.grid_size()[1], column=0, padx=5, pady=5)
        self.entry = Entry(root, width=30)
        self.entry.insert(0, "Add description...")
        self.entry.grid(row=root.grid_size()[1] - 2, column=0, padx=5, pady=5)
        self.checkbox = Checkbutton(root, variable=self.completed)
        self.checkbox.grid(row=root.grid_size()[1] - 1, column=2, padx=5, pady=5)
        self.delete_button = Button(root, text="Delete", command=self.delete_task)
        self.delete_button.grid(row=root.grid_size()[1] - 1, column=3, padx=5, pady=5)

    def delete_task(self):
        self.label.grid_forget()
        self.entry.grid_forget()
        self.checkbox.grid_forget()
        self.delete_button.grid_forget()
