
# DiskLog

**Stop guessing what's on your external drives.** DiskLog is a lightweight, fully customizable desktop application designed to track and manage collections of external disks, flash drives, and memory cards. Built entirely with Python's standard library, it offers a snappy, zero-dependency solution to digital hoarding.

What makes DiskLog special? **It is 100% config-driven.** You define your database schema and UI forms in a simple JSON file, and DiskLog automatically handles the rest, from rendering input fields to dynamically altering your SQLite database.

-----
![app preview screenshot](assets/app_screenshot.png)
-----
## ✨ Features

  * **🛠 Dynamic, Config-Driven UI:** Add, remove, or modify columns via a simple `config.json`. The app instantly generates the appropriate UI elements and updates the database schema automatically.
  * **📤 Flexible Data Export:** (New in v2.1.0) Export your filtered data to CSV for spreadsheets or to a brand-new SQLite database file for external use.
  * **🔍 Advanced Query Search:** Use powerful database operators directly in the search bar (e.g., `Type = SSD`, `is encrypted = 1`).
  * **✏️ In-App Schema Editor:** Tweak your configuration directly inside the app with built-in validation.
  * **⚡ Zero Dependencies:** Built strictly with Python's standard library. No `pip install` required.

-----

## 🚀 Getting Started

### 📦 Portable Version (Windows)
Download the latest `.exe` from the **Releases** page for a self-contained, no-installation experience.

### 🐍 Running from Source
**Requirements:** Python 3.10+ on Windows, macOS, or Linux.

1. Clone and enter the repository:
   ```bash
   git clone https://github.com/MohtadiAwada/DiskLog.git
   cd DiskLog
   ```

2. Run the application:
    ```bash
    python app.py
    ```

-----

## 📖 Special Features & Proper Usage

### 1\. The Export Engine (v2.1.0)

DiskLog now features a "What You See Is What You Get" export system. Only the data currently visible in your table (based on your search/filters) will be exported.

  * **Spreadsheet (.csv):** Generates a clean CSV file compatible with Excel, Google Sheets, and Numbers.
  * **Database File (.db):** Generates a new SQLite database. You can customize the **Table Name** and **Primary Key** during the export process, making it perfect for migrating specific datasets to other projects.

### 2\. Advanced Search Syntax

The search bar parses input to execute complex queries:

  * **Global Search:** Type any word to search across all columns.
  * **Targeted Operators:** Use `=`, `!=`, `>`, `<`, `>=`, `<=`, or `LIKE`.
      * *Example:* `Type != HDD`
  * **Multiple Queries:** Combine filters with a comma.
      * *Example:* `Type = Flash Drive, Sandisk`

### 3\. Automatic Schema Evolution

When you add a new column to the `columns` list in your config, DiskLog's engine automatically executes an `ALTER TABLE` command to update your SQLite database.

-----

## 🏗️ Project Architecture

```text
DiskLog/
├── app.py                 # Entry point (Initializes Tkinter mainloop)
├── config.json            # Auto-generated schema configuration
├── data.db                # Auto-generated SQLite database
├── core/                  # Backend Logic
│   ├── config.py          # Config loader and validator
│   ├── db.py              # Dynamic SQLite engine and query parser
│   └── store.py           # State management
├── models/                # Reusable UI Components
│   ├── table.py           # Dynamic data grid
│   ├── tools.py           # Toolbar buttons
│   └── export.py          # CSV and SQLite export engine (v2.1.0)
└── windows/               # Application Windows
    ├── main.py            # Main GUI layout
    ├── add_popup.py       # Dynamic creation form
    ├── edit_popup.py      # Dynamic edit form
    └── config_popup.py    # Raw JSON editor with safety validations
```

-----

## 📄 License

MIT License - see the [LICENSE](./LICENSE) file for details.