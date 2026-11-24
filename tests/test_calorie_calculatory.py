import pytest
from calorie_calculator import CalorieCalculator

calc = CalorieCalculator()


def test_lose_weight_target():
    # maintenance 2200, minus 700/day to lose 11 lbs in 55 days
    assert calc.daily_target(176, 165, 55, 1800, 400) == 1500


def test_gain_weight_target():
    assert calc.daily_target(150, 160, 50, 1800, 400) == 2900


def test_goal_date_in_past_rejected():
    with pytest.raises(ValueError):
        calc.daily_target(176, 165, 0, 1800, 400)


def test_negative_weight_rejected():
    with pytest.raises(ValueError):
        calc.daily_target(-5, 165, 55, 1800, 400)


def test_bmr_male():
    assert calc.bmr(176, 71, 30, "m") == 1780


def test_bmr_female():
    assert calc.bmr(176, 71, 30, "f") == 1614


def test_bmr_invalid_sex_rejected():
    with pytest.raises(ValueError):
        calc.bmr(176, 71, 30, "x")


def test_weekly_expected_change():
    assert calc.weekly_expected_change(176, 165, 55) == pytest.approx(-1.4)