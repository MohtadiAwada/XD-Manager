import tkinter as tk
from tkinter import ttk
from models.tools import load_tools

class MainWindow:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("DiskLog")
        
        self.search = tk.Frame(self.root)
        self.search.pack(side="top")
        tk.Label(self.search, text="Search:").pack(side="left")
        self.search_bar = tk.Entry(self.search)
        self.search_bar.pack(side="left")
        
        self.table = tk.Frame(self.root)
        self.table.pack(side="top")

        self.tools = tk.Frame(self.root)
        self.tools.pack(side="top")
        load_tools(self.tools)