import sqlite3
from contextlib import closing


class SqliteWeightRepository:
    """Stores goal-tracking weight entries (lbs) in the SQLite database."""

    def __init__(self, db_path="nutrition.db"):
        self.db_path = db_path
        with closing(sqlite3.connect(self.db_path)) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS goal_weights ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "entry_date TEXT NOT NULL, "
                "lbs REAL NOT NULL)"
            )
            conn.commit()

    def add(self, entry_date, lbs):
        with closing(sqlite3.connect(self.db_path)) as conn:
            conn.execute(
                "INSERT INTO goal_weights (entry_date, lbs) VALUES (?, ?)",
                (entry_date, lbs),
            )
            conn.commit()

    def all(self):
        with closing(sqlite3.connect(self.db_path)) as conn:
            rows = conn.execute(
                "SELECT entry_date, lbs FROM goal_weights ORDER BY entry_date, id"
            ).fetchall()
        return [{"date": d, "lbs": w} for d, w in rows]


class InMemoryWeightRepository:
    """Fake repository for tests. Same add()/all() interface, nothing touches disk."""

    def __init__(self, entries=None):
        self._entries = list(entries) if entries else []

    def add(self, entry_date, lbs):
        self._entries.append({"date": entry_date, "lbs": lbs})

    def all(self):
        return sorted(self._entries, key=lambda e: e["date"])