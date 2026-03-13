from datetime import date

from reimburse.citytype import CityType
from reimburse.project import Project
from reimburse.reimburse import calculate_reimbursement


def test_set1():
    expectedVal = 240
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 4), CityType.LOW)
    ]

    assert calculate_reimbursement(projects) == expectedVal

def test_set2():
    expectedVal = 665
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 2), date(2024, 10, 6), CityType.HIGH),
        Project(date(2024, 10, 6), date(2024, 10, 9), CityType.LOW)
    ]

    assert calculate_reimbursement(projects) == expectedVal

def test_set3():
    expectedVal = 520
    projects = [
        Project(date(2024, 9, 30), date(2024, 10, 3), CityType.LOW),
        Project(date(2024, 10, 5), date(2024, 10, 7), CityType.HIGH),
        Project(date(2024, 10, 8), date(2024, 10, 8), CityType.HIGH)
    ]

    assert calculate_reimbursement(projects) == expectedVal

def test_set4():
    expectedVal = 440
    projects = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 2), date(2024, 10, 3), CityType.HIGH),
        Project(date(2024, 10, 2), date(2024, 10, 6), CityType.HIGH)
    ]

    assert calculate_reimbursement(projects) == expectedVal

def test_set5():
    expectedVal = 0
    projects = []

    assert calculate_reimbursement(projects) == expectedVal

def test_set6():
    expectedVal = 0
    projects = [
        Project(date(2024, 10, 4), date(2024, 10, 1), CityType.LOW),
    ]

    assert calculate_reimbursement(projects) == expectedVal