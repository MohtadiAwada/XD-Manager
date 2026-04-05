import tkinter as tk
from tkinter import ttk
from windows.add_popup import addPopup

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
    
class Tools:
    def __init__(self, parent, store):
        self.tools = [
            {
                "name": "Add",
                "sign": "\u002B",
                "command": lambda: addPopup(store)
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
        self.frame = tk.Frame(parent)
        self.load_tools()
    def load_tools(self):
        for tool in self.tools:
            btn = tk.Button(self.frame, text=tool["sign"], command=tool["command"])
            btn.pack(side="right")
            ToolTip(btn, tool["name"])
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)