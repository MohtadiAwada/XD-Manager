import csv, sqlite3
import threading
import os
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from pathlib import Path

class Export:
    def __init__(self, store):
        messagebox.showinfo("Export Visible Data", "Only the visible data in the table will be exported.")
        self.popup = tk.Toplevel()
        #self.popup.geometry("200x200")
        self.popup.overrideredirect(True)
        self.popup.update_idletasks()

        root = self.popup.master
        x = root.winfo_rootx() + root.winfo_width()//2 - self.popup.winfo_width()//2
        y = root.winfo_rooty() + root.winfo_height()//2 - self.popup.winfo_height()//2
        self.popup.geometry(f"+{x}+{y}")

        self.popup.resizable(False, False)
        self.popup.grab_set()
        self.popup.focus_set()
        self.popup.bind("<Escape>", lambda e: self.popup.destroy())

        tk.Label(self.popup, text="Export").pack(side="top", pady=12)
        tk.Frame(self.popup, height=1, bg="#CCCCCC").pack(side="top", fill="x", padx=12, pady=[0, 6])
        name_frame = tk.Frame(self.popup)
        name_frame.pack(side="top", fill="x", padx=14, pady=[0, 6])
        tk.Label(name_frame, text="File Name:").pack(side="left", padx=[0, 6])
        self.file_name = tk.Entry(name_frame)
        self.file_name.pack(side="left", fill="x", expand=True)
        location_frame = tk.Frame(self.popup)
        location_frame.pack(side="top", fill="x", padx=14, pady=[0, 6])
        tk.Label(location_frame, text="Location:").pack(side="left", padx=[0, 6])
        self.file_location = tk.Entry(location_frame)
        self.file_location.pack(side="left", fill="x", expand=True)
        tk.Button(location_frame, text="\u2398", command=self.select_dir).pack(side="left", padx=[3, 0])
        type_frame = tk.Frame(self.popup)
        type_frame.pack(side="top", fill="x", padx=14, pady=[0, 6])
        tk.Label(type_frame, text="Export to:").pack(side="left", padx=[0, 6])
        self.file_type = ttk.Combobox(type_frame, values=["Table Sheet", "Database File"], state="readonly")
        self.file_type.set("Table Sheets")
        self.file_type.pack(side="left")
        tk.Frame(self.popup, height=1, bg="#CCCCCC").pack(side="top", fill="x", padx=12)
        tk.Button(self.popup, text="Export", command=self.handle_save).pack(side="top", fill="x", expand=True, padx=14, pady=[6, 0])
        tk.Button(self.popup, text="Cancel", command=self.popup.destroy).pack(side="top", fill="x", expand=True, padx=14, pady=[6, 12])

    def select_dir(self):
        file_dir = filedialog.askdirectory(title="Export", initialdir=Path.cwd())
        self.file_location.delete(0, "end")
        self.file_location.insert(0, file_dir)

    def handle_save(self):
        for input in [self.file_location, self.file_name]:
            if not input.get():
                messagebox.showwarning("Unvalid Input", "All fields are required.")
                return
        self.file_path = self.file_location.get()
        if not os.path.exists(self.file_path):
            messagebox.showwarning("Unvalid File Location", "the directory doesn't exits. please enter a valid path")
            return

        
    
    