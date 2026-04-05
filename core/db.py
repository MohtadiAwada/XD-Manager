import sqlite3

class DB:
    def __init__(self, file_path, columns):
        self.conn = sqlite3.connect(file_path)
        self.cursor = self.conn.cursor()
        self.columns = columns
        self.init_table()
    def init_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS disks (id_builtin INTEGER PRIMARY KEY AUTOINCREMENT)")
        self.conn.commit()
        self.cursor.execute("PRAGMA table_info(disks)")
        existing = [row[1] for row in self.cursor.fetchall()]
        for col in self.columns:
            if col["title"].replace(" ", "_") not in existing:
                self.cursor.execute(f"ALTER TABLE disks ADD COLUMN {col['title'].replace(" ", "_")} {col['db_type']}")
        self.conn.commit()
    def insert(self, data: dict):
        keys = [x.replace(" ", "_") for x in data.keys()]
        cols = ", ".join(keys)
        placeholders = ", ".join(["?" for _ in data])
        self.cursor.execute(f"INSERT INTO disks ({cols}) VALUES ({placeholders})", tuple(data.values()))
        self.conn.commit()
        self.print_table()
    def exists(self, col: str, value: str) -> bool:
        self.cursor.execute(f"SELECT 1 FROM disks WHERE {col} = ?", (value,))
        return self.cursor.fetchone() is not None
    def print_table(self):
        self.cursor.execute("SELECT * FROM disks")
        rows = self.cursor.fetchall()
        self.cursor.execute("PRAGMA table_info(disks)")
        headers = [row[1] for row in self.cursor.fetchall()]
        print(" | ".join(headers))
        print("-" * 50)
        for row in rows:
            print(" | ".join(str(v) for v in row))