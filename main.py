from tkinter import *
from tkinter.ttk import *
import sys
from views.view import View
import os
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from utils.systemUtils import SystemUtils
import xml.etree.ElementTree as ET
SystemUtils.add_to_sys_path(__file__)
class App:
    def __init__(self, title: str, geometry: tuple) -> None:
        self.instance: Tk = Tk()
        self.instance.title(title)
        self.instance.geometry(f"{str(geometry[0])}x{str(geometry[1])}")
        style: Style = Style(theme="darkly")
        self.view: View = View(self, "./views/home.xml")
        self.tasks: list = []
if __name__ == "__main__":
    app: App = App("Do", (500, 500))
    app.instance.mainloop()
