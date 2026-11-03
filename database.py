"""SQLite storage for MyNutritionBro. Data is saved in nutrition.db (created automatically)."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "nutrition.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS weight_logs (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   log_date TEXT NOT NULL,
                   weight REAL NOT NULL)"""
        )
        conn.execute(
            """CREATE TABLE IF NOT EXISTS food_logs (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   log_date TEXT NOT NULL,
                   food_name TEXT NOT NULL,
                   calories INTEGER NOT NULL)"""
        )


def add_weight(log_date, weight):
    with get_connection() as conn:
        conn.execute("INSERT INTO weight_logs (log_date, weight) VALUES (?, ?)", (log_date, weight))


def get_weights(newest_first=True):
    order = "DESC" if newest_first else "ASC"
    with get_connection() as conn:
        return conn.execute(
            f"SELECT * FROM weight_logs ORDER BY log_date {order}, id {order}"
        ).fetchall()


def add_food(log_date, food_name, calories):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO food_logs (log_date, food_name, calories) VALUES (?, ?, ?)",
            (log_date, food_name, calories),
        )


def get_foods():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM food_logs ORDER BY log_date DESC, id DESC").fetchall()
