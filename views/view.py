from tkinter import *
from tkinter.ttk import *
from tkinter import font
from todo.importance import Importance
import xml.etree.ElementTree as ET

class View:
    def __init__(self, root: Tk, xml_file: str):
        self.root: Tk = root
        self.xml_file: str = xml_file
        self.elements: dict = {}  # Dictionary to store elements by id
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
        title = self._create_widget(Label, element, text=element.get('text', ''),
                                    font=font.Font(family="Helvetica", size=20))
        title.grid(**self._get_grid_options(element))

    def create_button(self, element):
        button = self._create_widget(Button, element, text=element.get('text', ''), command=element.get(eval('command'), self.placeholder))
        button.grid(**self._get_grid_options(element))

    def create_entry(self, element):
        entry = self._create_widget(Entry, element, width=int(element.get('length', 0)))
        entry.grid(**self._get_grid_options(element))

    def create_radiobutton(self, element):
        value = element.get('value', '')  # Value for the radio button
        variable_id = element.get('variable', None)  # Get variable id if provided
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
        widget = widget_class(self.root, **kwargs)
        element_id = element.get('id')
        if element_id:
            self.elements[element_id] = widget  # Store widget by id if specified
        return widget

    def _get_grid_options(self, element):
        """Helper function to extract grid options from XML attributes."""
        return {
            'row': int(element.get('row', 0)),
            'column': int(element.get('column', 0)),
            'padx': int(element.get('padx', 0)),
            'pady': int(element.get('pady', 0)),
            'sticky': element.get('sticky', "")
        }

# Usage
# root = Tk()
# view = View(root, 'your_layout.xml')
# root.mainloop()
