import tkinter as tk
from tkinter import ttk
from windows.add_popup import addPopup

tools = [
    {
        "name": "Add",
        "sign": "\u002B",
        "command": lambda: addPopup()
    },
    {
        "name": "Delete",
        "sign": "\u2715",
        "command": None
    },
    {
        "name": "Edit",
        "sign": "\u270e",
        "command": None
    }
]

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)

    def show(self, event):
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        tk.Label(self.tooltip, text=self.text, padx=6, pady=3).pack()

    def hide(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def load_tools(parent:tk.Frame):
    for tool in tools:
        btn = tk.Button(parent, text=tool["sign"], command=tool["command"])
        btn.pack(side="right")
        ToolTip(btn, tool["name"])