# DiskLog

I have many external disks — most with dynamic content. I label each one with an ID, but over time I kept forgetting what each ID actually contained. So I built this app to track them.

---

## What's new in v2

v2 is a full rewrite of the original XD-Manager with a focus on functionality and a cleaner architecture.

- **SQLite** instead of JSON for data storage
- **Modular architecture** — core logic separated from UI
- **Config-driven** — table columns, form fields, and validation all defined in `config.json`
- **ttk Treeview** for the table — better performance and built-in selection
- Built with standard **Tkinter + ttk** instead of CustomTkinter

---

## Migrating from v1

v2 is not backwards compatible with v1's `data.json`. Your v1 data will not be automatically imported.

To keep your v1 data, the v1 release is still available under the `main` branch and in the [v1.2.0 release](../../releases).

---

## Project Structure

```
DiskLog/
├── app.py
├── config.json
├── data.db
├── core/
│   ├── config.py
│   ├── db.py
│   └── store.py
├── models/
│   └── tools.py
└── windows/
    ├── main.py
    └── add_popup.py
```

---

## Getting Started

**Requirements:**
- Python 3.10+
- No external dependencies — uses only the Python standard library

**Run:**
```bash
python app.py
```

---

## Configuration

Everything is driven by `config.json`. You can add, remove, or rename columns without touching the code.

```json
{
    "db_path": "data.db",
    "columns": [
        {
            "title": "ID",
            "type": "entry",
            "db_type": "TEXT",
            "pattern": "^\\d{4}$",
            "required": true,
            "unique": true
        }
    ]
}
```

**Column options:**

| Key | Description |
|---|---|
| `title` | Display name and database column name |
| `type` | Input type: `entry`, `select`, `checkbox` |
| `db_type` | SQLite type: `TEXT`, `INTEGER`, `REAL` |
| `required` | If true, field cannot be empty |
| `unique` | If true, value must not already exist |
| `pattern` | Regex pattern for format validation |
| `values` | Options list for `select` type |

---

## Features

- Add, delete, and browse disk entries
- Config-driven columns and form fields
- Input validation with pattern matching
- Data stored locally in SQLite

**Coming soon:**
- Search bar
- Edit existing entries

---

## Tech Stack

- Python 3
- Tkinter + ttk
- SQLite

---

## License

MIT