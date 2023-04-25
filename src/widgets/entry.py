from gi.repository import Adw
from ..globals import data
from ..data import UserData
from .todo import Todo


class Entry(Adw.PreferencesPage):
    def __init__(self):
        super().__init__()
        self.entry = Adw.EntryRow(title="Add new task")
        self.entry.connect("entry-activated", self.on_entry_activated)

        self.group = Adw.PreferencesGroup()
        self.group.add(self.entry)

        self.add(self.group)

    def on_entry_activated(self, entry):
        # Check for empty string
        if entry.props.text == "":
            return
        new_data = UserData.get()
        # Check if todo exists
        if entry.props.text in new_data["todos"]:
            return
        # Add new todo
        new_data["todos"][entry.props.text] = {"sub": [], "color": ""}
        UserData.set(new_data)
        data["todo_list"].add(Todo(entry.props.text))
        entry.props.text = ""
