import tkinter as tk
from tkinter import ttk
from models.tools import Tools
from windows.table import Table
from core.store import Store

store = Store()
class MainWindow:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("DiskLog")
        
        self.search = tk.Frame(self.root)
        self.search.pack(side="top")
        tk.Label(self.search, text="Search:").pack(side="left")
        self.search_bar = tk.Entry(self.search)
        self.search_bar.pack(side="left")
        
        self.table = Table(self.root, store)
        self.table.pack(side="top", fill="both", expand=True)

        self.tools = Tools(self.root, store)
        self.tools.pack(side="top", fill="x")