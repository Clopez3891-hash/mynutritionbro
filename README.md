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


## Sprint 2: Daily calorie target

### New prerequisites
- Run `pip install -r requirements.txt` (now includes pytest).

### Try the new feature
1. From the project root, run `python goal_cli.py`.
2. Choose 1 to log your weight in lbs (press Enter for today's date).
3. Choose 2 and enter goal weight (lbs), a future goal date (YYYY-MM-DD), height (inches), age, sex (m/f), and activity calories. Your daily calorie target is shown. A past goal date shows an error.

### Run the automated tests
From the project root: `python -m pytest -v`

### Known limitations
- Goal settings are entered each time, not saved.
- The estimate uses 3,500 calories per pound.
- This menu is separate from the Sprint 1 app screens; both use the same nutrition.db.
- Not done this sprint (planned for Sprint 3): weight history with date filtering, weekly calorie adjustment suggestions, and connecting the calorie target to the main app pages.