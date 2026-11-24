from datetime import date

import pytest
from calorie_calculator import CalorieCalculator
from goal_service import GoalService
from weight_repository import InMemoryWeightRepository

TODAY = date(2026, 11, 23)
GOAL_DATE = date(2027, 1, 17)  # exactly 55 days after TODAY


def make_service(entries=None):
    return GoalService(InMemoryWeightRepository(entries), CalorieCalculator())


def test_daily_target_for_weight_loss():
    service = make_service([{"date": "2026-11-23", "lbs": 176.0}])
    # BMR 1780 + activity 400 - 700/day deficit = 1480
    assert service.daily_target(165, GOAL_DATE, 71, 30, "m", 400, today=TODAY) == 1480


def test_daily_target_rejects_past_goal_date():
    service = make_service([{"date": "2026-11-23", "lbs": 176.0}])
    with pytest.raises(ValueError):
        service.daily_target(165, date(2026, 11, 20), 71, 30, "m", 400, today=TODAY)


def test_daily_target_requires_a_logged_weight():
    with pytest.raises(ValueError):
        make_service().daily_target(165, GOAL_DATE, 71, 30, "m", 400, today=TODAY)


def test_log_weight_saves_entry():
    service = make_service()
    service.log_weight("2026-11-23", 176.0)
    assert service.latest_weight() == 176.0


def test_log_weight_rejects_negative():
    with pytest.raises(ValueError):
        make_service().log_weight("2026-11-23", -1)


def test_log_weight_rejects_bad_date_format():
    with pytest.raises(ValueError):
        make_service().log_weight("11/23/2026", 176.0)