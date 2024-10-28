from tkinter import *
from tkinter.ttk import *
from tkinter import font
from commands.addTodo import add_task
from todo.importance import Importance
import xml.etree.ElementTree as ET

class View:
    def __init__(self, main, xml_file: str): # main is an instance of App but due to circular import problems I was unable to import App
        self.root: Tk = main.instance
        self.xml_file: str = xml_file
        self.elements: dict = {} # Dictionary to store elements by id
        self.main = main 
        self.create_widgets()
    def placeholder(self):
        pass
    def create_widgets(self):
        tree: ET.ElementTree = ET.parse(self.xml_file)
        root: ET.Element = tree.getroot() 
        for element in root:
            if element.tag == "window":
                self.root.title(element.get('title', ''))
        for element in root.find('layout'):
            if element.tag == "label":
                self.create_label(element)
            elif element.tag == "title":
                self.create_title(element)
            elif element.tag == "button":
                self.create_button(element)
            elif element.tag == "entry":
                self.create_entry(element)
            elif element.tag == "radiobutton":
                self.create_radiobutton(element)

    def create_label(self, element):
        label = self._create_widget(Label, element, text=element.get('text', ''))
        label.grid(**self._get_grid_options(element))

    def create_title(self, element):
        title = self._create_widget(Label, element, text=element.get('text', ''), font=font.Font(family="Helvetica", size=20))
        title.grid(**self._get_grid_options(element))

    def create_button(self, element):
        command_name = element.get('command', 'self.placeholder')
        args_str = element.get('args', '')
        # Set up some predefined variables to be used.
        safe_context = {
            'root': self.main,
            'elements': self.elements,
            'add_task': add_task,
            'self': self,
        }
        command_function = safe_context.get(command_name) or getattr(self, command_name, self.placeholder)
        command_args = eval(f'({args_str})', safe_context)
        button = self._create_widget(Button, element, text=element.get('text', ''),
                                    command=lambda: command_function(*command_args))
        button.grid(**self._get_grid_options(element))


    def create_entry(self, element):
        entry = self._create_widget(Entry, element, width=int(element.get('length', 0)))
        entry.grid(**self._get_grid_options(element))

    def create_radiobutton(self, element):
        value = element.get('value', '')
        variable_id = element.get('variable', None)
        if variable_id:
            if variable_id not in self.elements:
                self.elements[variable_id] = StringVar()
            var = self.elements[variable_id]
        else:
            var = StringVar()
        radiobutton = self._create_widget(Radiobutton, element, text=element.get('text', ''),
                                          variable=var, value=value)
        radiobutton.grid(**self._get_grid_options(element))

    def _create_widget(self, widget_class, element, **kwargs):
        element_id = element.get('id')
        widget = widget_class(self.root, **kwargs)
        if element_id:
            self.elements[element_id] = widget  # Store widget by id if specified
        return widget

    def _get_grid_options(self, element):
        """Helper function to extract grid options from XML attributes. This used to be repeated in all create funcs lol."""
        return {
            'row': int(element.get('row', 0)),
            'column': int(element.get('column', 0)),
            'padx': int(element.get('padx', 0)),
            'pady': int(element.get('pady', 0)),
            'sticky': element.get('sticky', "")
        }

