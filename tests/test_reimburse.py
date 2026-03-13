from datetime import date

from reimburse.citytype import CityType
from reimburse.project import Project
from reimburse.reimburse import _find_travel_days, calculate_reimbursement


def test_set1():
    expected_val = 240
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 4), CityType.LOW)
    ]

    result = calculate_reimbursement(projects)
    print(f"\nSet 1 result: ${result}")
    assert result == expected_val


def test_set2():
    expected_val = 665
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 2), date(2024, 10, 6), CityType.HIGH),
        Project(date(2024, 10, 6), date(2024, 10, 9), CityType.LOW)
    ]

    result = calculate_reimbursement(projects)
    print(f"\nSet 2 result: ${result}")
    assert result == expected_val


def test_set3():
    expected_val = 520
    projects = [
        Project(date(2024, 9, 30), date(2024, 10, 3), CityType.LOW),
        Project(date(2024, 10, 5), date(2024, 10, 7), CityType.HIGH),
        Project(date(2024, 10, 8), date(2024, 10, 8), CityType.HIGH)
    ]

    result = calculate_reimbursement(projects)
    print(f"\nSet 3 result: ${result}")
    assert result == expected_val


def test_set4():
    expected_val = 440
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 2), date(2024, 10, 3), CityType.HIGH),
        Project(date(2024, 10, 2), date(2024, 10, 6), CityType.HIGH)
    ]

    result = calculate_reimbursement(projects)
    print(f"\nSet 4 result: ${result}")
    assert result == expected_val


def test_set5():
    expected_val = 0
    projects = []

    result = calculate_reimbursement(projects)
    print(f"\nSet 5 result: ${result}")
    assert result == expected_val


def test_set6():
    expected_val = 0
    projects = [
        Project(date(2024, 10, 4), date(2024, 10, 1), CityType.LOW),
    ]

    result = calculate_reimbursement(projects)
    print(f"\nSet 6 result: ${result}")
    assert result == expected_val


def test_set7():
    expected_val = 4
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 2), date(2024, 10, 6), CityType.HIGH),
        Project(date(2024, 10, 6), date(2024, 10, 9), CityType.LOW),
        Project(date(2024, 10, 13), date(2024, 10, 14), CityType.LOW),
        Project(date(2024, 10, 14), date(2024, 10, 14), CityType.LOW),
        Project(date(2024, 10, 15), date(2024, 10, 16), CityType.LOW),
        Project(date(2024, 10, 13), date(2024, 10, 19), CityType.LOW)
    ]

    result = len(_find_travel_days(projects))
    print(f"\nSet 7 travel days: {result}")
    assert result == expected_val


def test_set8():
    expected_travel_days = 0
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
    ]

    result = len(_find_travel_days(projects))
    print(f"\nSet 8 travel days: {result}")
    assert result == expected_travel_days

    expected_val = 75
    result = calculate_reimbursement(projects)
    print(f"Set 8 result: ${result}")
    assert result == expected_val


def test_set9():
    expected_travel_days = 0
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.HIGH),
    ]

    result = len(_find_travel_days(projects))
    print(f"\nSet 9 travel days: {result}")
    assert result == expected_travel_days

    expected_val = 85
    result = calculate_reimbursement(projects)
    print(f"Set 9 result: ${result}")
    assert result == expected_val


def test_set10():
    expected_travel_days = 2
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 13), CityType.LOW),
        Project(date(2024, 10, 3), date(2024, 10, 5), CityType.LOW),
        Project(date(2024, 10, 12), date(2024, 10, 15), CityType.HIGH),
    ]

    result = len(_find_travel_days(projects))
    print(f"\nSet 10 travel days: {result}")
    assert result == expected_travel_days

    expected_val = 1105
    result = calculate_reimbursement(projects)
    print(f"Set 10 result: ${result}")
    assert result == expected_val


def test_set11():
    expected_travel_days = 4
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 13), CityType.LOW),
        Project(date(2024, 10, 3), date(2024, 10, 5), CityType.LOW),
        Project(date(2024, 10, 12), date(2024, 10, 15), CityType.HIGH),
        Project(date(2024, 10, 12), date(2024, 10, 15), CityType.LOW),
        Project(date(2024, 10, 17), date(2024, 10, 20), CityType.HIGH),
        Project(date(2024, 10, 19), date(2024, 10, 22), CityType.LOW),
    ]

    travel_days = _find_travel_days(projects)
    print(f"\nSet 11 travel days: {len(travel_days)}")
    assert len(travel_days) == expected_travel_days

    expected_val = 1535
    result = calculate_reimbursement(projects)
    print(f"Set 11 result: ${result}")
    assert result == expected_val
