# MyNutritionBro

A fitness/nutrition tracker for logging weight and food. Built for CS 319 by **Cristian Lopez**.
Sprint 1 delivers a working weight log and food log that save to a local database.

## Technologies
Python, Flask, SQLite (built into Python), HTML/CSS (Jinja templates).

## Prerequisites
- Python 3.10 or newer (`python --version`)
- pip (included with Python)

## Installation
From the project root folder (the one containing `app.py`):

```
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

## Configuration
None required. The SQLite database file `nutrition.db` is created automatically on first run.

## Running the application
```
python app.py
```
Open http://127.0.0.1:5000 in a browser. You should see the Weight Log page.
Stop the app with Ctrl+C.

## Trying the Sprint 1 functionality
1. On **Weight Log**, enter a date and a weight (e.g. 180.5) and click Add Weight. It appears in the table.
2. Try an empty or invalid weight (e.g. `abc`, `0`, `-5`). An error appears and nothing is saved.
3. Use "Newest first" / "Oldest first" to sort entries by date.
4. On **Food Log**, enter a food and calories (e.g. Oatmeal, 300) and click Add Food.
5. Try an empty food name or non-numeric calories to see validation errors.
6. Refresh the page or restart the app. Saved entries remain.

## Known limitations
- No login yet; all entries belong to one local user.
- No dashboard, graphs, goals, or calorie calculations yet.
- Entries cannot be edited or deleted yet.
- Weight is entered in pounds only.
