# DiskLog

Stop guessing what's on your external drives. DiskLog is a lightweight desktop app for tracking and managing collections of external disks, flash drives, and memory cards. Built entirely on Python's standard library — no pip install, no setup, just run it.

What makes DiskLog different is that it is **100% config-driven**. You define your database schema and form fields in a single JSON file, and the app builds itself around it — from the UI form inputs to the SQLite table structure.

---

![app screenshot](assets/app_screenshot.png)

---

## Features

**Config-driven UI and database** — Add, remove, or rename columns in `config.json` and the app adapts automatically. The form, table, and database schema all update to match without touching any code.

**Advanced search syntax** — The search bar parses real database operators. You can search globally across all columns, or use targeted queries like `Type = SSD`, `Type != HDD`, or combine filters with commas: `Type = Flash Drive, Sandisk`.

**Export engine** — Export exactly what is visible in the table (based on your current search or filter) to two formats:

- **Spreadsheet (.csv)** — compatible with Excel, Google Sheets, and Numbers

- **Database file (.db)** — generates a new portable SQLite database with a custom table name and primary key column

**Automatic schema evolution** — When you add a new column to your config, DiskLog runs `ALTER TABLE` automatically to update your existing database. No data is lost.

**In-app config editor** — Edit your `config.json` directly inside the app with a built-in JSON editor. Includes validation, a reset-to-default option, and a safety confirmation before applying changes.

**Input validation** — Per-column rules defined in config: required fields, regex pattern matching, and uniqueness checks. Errors are shown before anything hits the database.

**Multi-row delete** — Select one or more rows in the table and delete them in a single action.

---

## Getting Started

Requires Python 3.10+ on Windows, macOS, or Linux.

```bash
git clone https://github.com/MohtadiAwada/DiskLog.git
cd DiskLog
python app.py
```

---

## Search Syntax

| Query | Behavior |
| --- | --- |
| `backup` | Global search across all columns |
| `Type = SSD` | Exact match on a specific column |
| `Type != HDD` | Not equal |
| `Type LIKE Flash%` | Pattern match |
| `Type = Flash Drive, Sandisk` | Multiple filters combined with AND |

Supported operators: `=`, `!=`, `<`, `>`, `<=`, `>=`, `LIKE`

---

## Configuration

Everything is defined in `config.json`. A column entry looks like this:

```json
{
    "title": "ID",
    "type": "entry",
    "db_type": "TEXT",
    "pattern": "^\\d{4}$",
    "required": true,
    "unique": true
}
```

**Column options:**

| Key | Description |
| --- | --- |
| `title` | Display name and database column name |
| `type` | Input widget: `entry`, `select`, or `checkbox` |
| `db_type` | SQLite type: `TEXT`, `INTEGER`, `REAL`, etc. |
| `required` | Field cannot be empty on submit |
| `unique` | Value must not already exist in the database |
| `pattern` | Regex pattern for format validation |
| `values` | List of options, required for `select` type |

---

## Project Structure

```text
DiskLog/
├── app.py                 # Entry point
├── config.json            # Schema configuration
├── data.db                # SQLite database (auto-created)
├── core/
│   ├── config.py          # Config loader and validator
│   ├── db.py              # SQLite engine and query parser
│   └── store.py           # Shared state
├── models/
│   ├── table.py           # Data table component
│   ├── tools.py           # Toolbar buttons
│   └── export.py          # CSV and SQLite export engine
└── windows/
    ├── main.py            # Main window layout
    ├── add_popup.py       # Add entry form
    ├── edit_popup.py      # Edit entry form
    └── config_popup.py    # In-app JSON config editor
```

---

## Migrating from v1 (XD-Manager)

v2 is a full rewrite and is not backwards compatible with v1's `data.json`. Your v1 data will not be automatically imported. The v1 release is still available on the `main` branch and in the [v1.2.0 release](../../releases).

---

## Tech Stack

- Python 3.10+
- Tkinter + ttk
- SQLite3
- JSON

---

## License

MIT — see [LICENSE](./LICENSE) for details.
