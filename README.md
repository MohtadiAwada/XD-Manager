# XD-Manager

I have many external disks — most with dynamic content. I label each one with an ID, but over time I kept forgetting what each ID actually contained. So I built this app to track them.

---

## Features

- Log external disks with an ID, title, type, and description
- Mark devices as encrypted and note the password protocol used
- Select and delete entries from the table
- Data is stored locally — no internet, no account

**Coming soon:**
- Customizable table columns
- Search bar
- Edit existing entries

---

## Getting Started

Go to the `dist/` folder and run `External-Disks-Manager.exe`.  
No installation required.

> Make sure `data.json` is in the same folder as the `.exe` on first run — it will be created automatically after your first save.

---

## Project Structure

```
XD-Manager/
├── app.py
├── LICENSE
├── .gitignore
├── README.md
└── dist/
    ├── External-Disks-Manager.exe
    └── icon.ico
```

---

## Tech Stack

- Python 3
- CustomTkinter
- JSON (local storage)

---

## License

MIT