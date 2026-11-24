from weight_repository import InMemoryWeightRepository, SqliteWeightRepository


def test_sqlite_repository_round_trip_sorted(tmp_path):
    repo = SqliteWeightRepository(str(tmp_path / "test.db"))
    repo.add("2026-11-22", 175.0)
    repo.add("2026-11-20", 176.0)
    assert repo.all() == [
        {"date": "2026-11-20", "lbs": 176.0},
        {"date": "2026-11-22", "lbs": 175.0},
    ]


def test_in_memory_repository_sorted():
    repo = InMemoryWeightRepository()
    repo.add("2026-11-22", 175.0)
    repo.add("2026-11-20", 176.0)
    assert [e["lbs"] for e in repo.all()] == [176.0, 175.0]