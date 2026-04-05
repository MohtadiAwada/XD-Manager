import tkinter as tk
from tkinter import ttk
from core.store import Store
import re

field_types = {
    "entry": lambda parent, col: tk.Entry(parent),
    "select": lambda parent, col: ttk.Combobox(parent, values=col["values"], state="readonly"),
    "checkbox": lambda parent, col: setattr(w := tk.Checkbutton(parent), "var", tk.BooleanVar()) or w
}

store = Store()

class addPopup:
    def __init__(self):
        self.popup = tk.Toplevel()
        self.popup.title("Add Disk")
        self.popup.grab_set()
        self.popup.focus_set()

        self.field_widgets = []
        self.biuld_from()

    def biuld_from(self):
        for col in store.config.get("columns"):
            frame = tk.Frame(self.popup)
            frame.pack(side="top")
            tk.Label(frame, text=col["title"]+":").pack(side="left")
            field = field_types[col["type"]](frame, col)
            field.pack(side="left")
            self.field_widgets.append(field)
        frame = tk.Frame(self.popup)
        frame.pack(side="top")
        tk.Button(frame, text="save", command=self.handle_save).pack(side="right")
        tk.Button(frame, text="cancel", command=self.handle_cancel).pack(side="left")
    def handle_cancel(self):
        self.popup.destroy()
    def handle_save(self):
        data = {}
        for widget, col in zip(self.field_widgets, store.config.get("columns")):
            if isinstance(widget, tk.Checkbutton):
                data[col["title"]] = int(widget.var.get())
            else:
                data[col["title"]] = widget.get()
        
        error = self.validate(data)
        if error:
            #self.error_lbl.configure(text=error)
            return
        store.db.insert(data)
        self.popup.destroy()
    def validate(self, data: dict) -> str | None:
        for col in store.config.get("columns"):
            value = data.get(col["title"], "")
            if col.get("required") and not value:
                return f"{col['title']} is required"
            if col.get("pattern") and not re.match(col["pattern"], str(value)):
                return f"{col['title']} has wrong format"
            if col.get("unique") and store.db.exists(col["title"], value):
                return f"{col['title']} already exists"
        return None