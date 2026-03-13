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
    expected_travel_days = 1
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
    ]

    result = len(_find_travel_days(projects))
    print(f"\nSet 8 travel days: {result}")
    assert result == expected_travel_days

    expected_val = 45
    result = calculate_reimbursement(projects)
    print(f"Set 8 result: ${result}")
    assert result == expected_val


def test_set9():
    expected_travel_days = 1
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.HIGH),
    ]

    result = len(_find_travel_days(projects))
    print(f"\nSet 9 travel days: {result}")
    assert result == expected_travel_days

    expected_val = 55
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


def test_set12():
    expected_travel_days = 2
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 13), CityType.LOW),
        # invalid project start & end dates
        Project(date(2024, 10, 8), date(2024, 10, 5), CityType.LOW),
    ]

    travel_days = _find_travel_days(projects)
    print(f"\nSet 12 travel days: {len(travel_days)}")
    assert len(travel_days) == expected_travel_days

    expected_val = 915
    result = calculate_reimbursement(projects)
    print(f"Set 12 result: ${result}")
    assert result == expected_val


def test_set13():
    expected_travel_days = 1
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.HIGH),
    ]

    travel_days = _find_travel_days(projects)
    print(f"\nSet 13 travel days: {len(travel_days)}")
    assert len(travel_days) == expected_travel_days

    expected_val = 55
    result = calculate_reimbursement(projects)
    print(f"Set 13 result: ${result}")
    assert result == expected_val


def test_set14():
    expected_travel_days = 2
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 10), CityType.HIGH),
        Project(date(2024, 10, 11), date(2024, 10, 20), CityType.HIGH),
    ]

    travel_days = _find_travel_days(projects)
    print(f"\nSet 14 travel days: {len(travel_days)}")
    assert len(travel_days) == expected_travel_days

    expected_val = 1640
    result = calculate_reimbursement(projects)
    print(f"Set 14 result: ${result}")
    assert result == expected_val


def test_set15():
    expected_travel_days = 2
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 10), CityType.LOW),
        Project(date(2024, 10, 11), date(2024, 10, 20), CityType.LOW),
    ]

    travel_days = _find_travel_days(projects)
    print(f"\nSet 15 travel days: {len(travel_days)}")
    assert len(travel_days) == expected_travel_days

    expected_val = 1440
    result = calculate_reimbursement(projects)
    print(f"Set 15 result: ${result}")
    assert result == expected_val


def test_set16():
    expected_travel_days = 2
    projects = [
        Project(date(2024, 10, 1), date(2025, 10, 5), CityType.LOW),
    ]

    travel_days = _find_travel_days(projects)
    print(f"\nSet 16 travel days: {len(travel_days)}")
    assert len(travel_days) == expected_travel_days

    expected_val = 27690
    result = calculate_reimbursement(projects)
    print(f"Set 16 result: ${result}")
    assert result == expected_val


def test_set17():
    expected_travel_days = 4
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 5), CityType.HIGH),
        Project(date(2024, 11, 1), date(2024, 12, 5), CityType.LOW),
    ]

    travel_days = _find_travel_days(projects)
    print(f"\nSet 17 travel days: {len(travel_days)}")
    assert len(travel_days) == expected_travel_days

    expected_val = 2930
    result = calculate_reimbursement(projects)
    print(f"Set 17 result: ${result}")
    assert result == expected_val


def test_set18():
    expected_travel_days = 0
    projects = [
        Project(date(2025, 10, 1), date(2024, 10, 5), CityType.HIGH),
        Project(date(2025, 11, 1), date(2024, 12, 5), CityType.LOW),
    ]

    travel_days = _find_travel_days(projects)
    print(f"\nSet 18 travel days: {len(travel_days)}")
    assert len(travel_days) == expected_travel_days

    expected_val = 0
    result = calculate_reimbursement(projects)
    print(f"Set 18 result: ${result}")
    assert result == expected_val
