from datetime import date


class GoalService:
    """Coordinates weight data and calorie math. Receives its dependencies."""

    def __init__(self, repository, calculator):
        self.repository = repository
        self.calculator = calculator

    def log_weight(self, entry_date, lbs):
        date.fromisoformat(entry_date)  # raises ValueError for bad formats
        if lbs <= 0:
            raise ValueError("Weight must be positive")
        self.repository.add(entry_date, lbs)

    def latest_weight(self):
        entries = self.repository.all()
        if not entries:
            raise ValueError("Log your weight first")
        return entries[-1]["lbs"]

    def daily_target(self, goal_lbs, goal_date, height_in, age, sex,
                     activity_kcal, today=None):
        today = today or date.today()
        current = self.latest_weight()
        bmr = self.calculator.bmr(current, height_in, age, sex)
        days_left = (goal_date - today).days
        return self.calculator.daily_target(
            current, goal_lbs, days_left, bmr, activity_kcal
        )