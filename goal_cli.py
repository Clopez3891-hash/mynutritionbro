from datetime import date

from calorie_calculator import CalorieCalculator
from goal_service import GoalService
from weight_repository import SqliteWeightRepository


def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def ask_date(prompt):
    while True:
        try:
            return date.fromisoformat(input(prompt))
        except ValueError:
            print("Use the format YYYY-MM-DD.")


def log_weight(service):
    raw = input("Date (YYYY-MM-DD, or press Enter for today): ").strip()
    entry_date = raw or date.today().isoformat()
    lbs = ask_float("Weight in lbs: ")
    try:
        service.log_weight(entry_date, lbs)
        print("Weight saved.")
    except ValueError as err:
        print(f"Error: {err}")


def show_daily_target(service):
    goal_lbs = ask_float("Goal weight in lbs: ")
    goal_date = ask_date("Goal date (YYYY-MM-DD): ")
    height_in = ask_float("Height in inches (5'10\" = 70): ")
    age = ask_float("Age: ")
    sex = input("Sex (m/f): ").strip().lower()
    activity = ask_float("Calories burned from daily activity (e.g. 400): ")
    try:
        target = service.daily_target(goal_lbs, goal_date, height_in, age, sex, activity)
        print(f"Your daily calorie target: {target} kcal")
    except ValueError as err:
        print(f"Error: {err}")


def main():
    service = GoalService(SqliteWeightRepository("nutrition.db"), CalorieCalculator())
    while True:
        print("\n1) Log weight\n2) Daily calorie target\n0) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            log_weight(service)
        elif choice == "2":
            show_daily_target(service)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()