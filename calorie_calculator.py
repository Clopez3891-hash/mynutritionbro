class CalorieCalculator:
    """Calculates calorie numbers using US units. No input(), print(), or file access here."""

    KCAL_PER_LB = 3500      # approx. calories in 1 lb of body weight
    LB_TO_KG = 0.45359237
    IN_TO_CM = 2.54

    def bmr(self, weight_lbs, height_in, age, sex):
        """Mifflin-St Jeor estimate. Takes lbs and inches. sex is 'm' or 'f'."""
        if weight_lbs <= 0 or height_in <= 0 or age <= 0:
            raise ValueError("Weight, height, and age must be positive")
        if sex not in ("m", "f"):
            raise ValueError("Sex must be 'm' or 'f'")
        kg = weight_lbs * self.LB_TO_KG
        cm = height_in * self.IN_TO_CM
        base = 10 * kg + 6.25 * cm - 5 * age
        return round(base + 5 if sex == "m" else base - 161)

    def daily_target(self, current_lbs, goal_lbs, days_left, bmr, activity_kcal):
        if days_left <= 0:
            raise ValueError("Goal date must be in the future")
        if current_lbs <= 0 or goal_lbs <= 0:
            raise ValueError("Weights must be positive")
        daily_adjust = ((goal_lbs - current_lbs) * self.KCAL_PER_LB) / days_left
        return round(bmr + activity_kcal + daily_adjust)

    def weekly_expected_change(self, current_lbs, goal_lbs, days_left):
        """Expected lbs change per week to reach the goal on time."""
        if days_left <= 0:
            raise ValueError("Goal date must be in the future")
        return (goal_lbs - current_lbs) / days_left * 7