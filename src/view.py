from tkinter import *
from tkinter.ttk import *
from tkinter import font
from addTodo import add_task
from importance import Importance
import xml.etree.ElementTree as ET
"""This class reads an xml file and grids tkinter elements! how epic"""
class View:
    def __init__(self, main, xml_file: str) -> None: # main is an instance of App but due to circular import problems I was unable to import App
        self.root: Tk = main.instance
        self.xml_file: str = xml_file
        self.elements: dict = {} # Dictionary to store elements by id
        self.main = main # App.
        self.create_widgets()
    def placeholder(self) -> None: ...
    def create_widgets(self) -> None:
        tree: ET.ElementTree = ET.parse(self.xml_file)
        root: ET.Element = tree.getroot() 
        for element in root:
            if element.tag == "window":
                self.root.title(element.get('title', ''))
        for element in root.find('layout'):
            if element.tag == "label": # I hate python 3.9 where switch- i mean "match" statements don't eixst.
                self.create_label(element)
            elif element.tag == "title":
                self.create_title(element)
            elif element.tag == "button":
                self.create_button(element)
            elif element.tag == "entry":
                self.create_entry(element)
            elif element.tag == "radiobutton":
                self.create_radiobutton(element)
            elif element.tag == "seperator":
                self.create_seperator(element)

    def create_label(self, element: ET.Element) -> None:
        label: Label = self._create_widget(Label, element, text=element.get('text', ''))
        label.grid(**self._get_grid_options(element))

    def create_title(self, element: ET.Element) -> None:
        title: Label = self._create_widget(Label, element, text=element.get('text', ''), font=font.Font(family="Helvetica", size=20))
        title.grid(**self._get_grid_options(element))

    def create_button(self, element: ET.Element) -> None:
        command_name: str = element.get('command', 'self.placeholder')
        args_str: str = element.get('args', '')
        # Set up some predefined variables to be used.
        safe_context: dict = {
            'root': self.main,
            'elements': self.elements,
            'add_task': add_task,
            'self': self,
        }
        command_function = safe_context.get(command_name) or getattr(self, command_name, self.placeholder)
        command_args: tuple = eval(f'({args_str})', safe_context)
        button: Button = self._create_widget(Button, element, text=element.get('text', ''),
                                    command=lambda: command_function(*command_args))
        button.grid(**self._get_grid_options(element))


    def create_entry(self, element: ET.Element) -> None:
        entry: Entry = self._create_widget(Entry, element, width=int(element.get('length', 0)))
        entry.grid(**self._get_grid_options(element))
    def create_seperator(self, element: ET.Element) -> None:
        orient: str = element.get('orient', 'horizontal')
        if orient not in ["horizontal", "vertical"]:
            print(f"Warning: Invalid orient '{orient}', defaulting to 'horizontal'")
            orient = "horizontal"
        separator: Separator = self._create_widget(Separator, element, orient=orient)
        grid_options = self._get_grid_options(element)
        if 'columnspan' not in grid_options:
            grid_options['columnspan'] = 10
            grid_options['sticky'] = 'ew'
        
        separator.grid(**grid_options)


    def create_radiobutton(self, element: ET.Element) -> None:
        value: str = element.get('value', '')
        variable_id: str = element.get('variable', None)
        if variable_id:
            if variable_id not in self.elements:
                self.elements[variable_id] = StringVar()
            var: StringVar = self.elements[variable_id]
        else:
            var = StringVar()
        radiobutton: Radiobutton = self._create_widget(Radiobutton, element, text=element.get('text', ''),
                                          variable=var, value=value)
        radiobutton.grid(**self._get_grid_options(element))

    def _create_widget(self, widget_class, element, **kwargs):
        element_id: str = element.get('id') or str(len(self.elements) + 1)
        widget = widget_class(self.root, **kwargs)
        self.elements[element_id] = widget
        return widget


    def _get_grid_options(self, element) -> dict:
        """Helper function to extract grid options from XML attributes. This used to be repeated in all create methods lol."""
        return {
            'row': int(element.get('row', 0)),
            'column': int(element.get('column', 0)),
            'padx': int(element.get('padx', 0)),
            'pady': int(element.get('pady', 0)),
            'ipadx': int(element.get('ipadx', 0)),
            'ipady': int(element.get('ipady', 0)),
            'sticky': element.get('sticky', "")
        }