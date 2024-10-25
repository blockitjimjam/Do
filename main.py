from tkinter import *
from tkinter.ttk import *
from views.view import *
from ttkbootstrap import Style
from ttkbootstrap.constants import *
import xml.etree.ElementTree as ET
class App:
    def __init__(self, title: str, geometry: tuple):
        self.instance: Tk = Tk()
        self.instance.title(title)
        self.instance.geometry(f"{str(geometry[0])}x{str(geometry[1])}")
        style: Style = Style(theme="darkly")
        self.view: View = View(self.instance, "./views/home.xml")
app: App = App("Do", (500, 500))
app.instance.mainloop()
