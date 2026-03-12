from datetime import date
from reimburse.citytype import CityType
from reimburse.project import Project
from reimburse.reimburse import Reimburse

def test_set1():
    projects = [
        Project(date(24, 10, 1), date(24, 10, 4), CityType.LOW)
    ]
    assert Reimburse(projects).calculate_reimburstment() == -1

def test_set2():
    projects = [
        Project(date(24, 10, 1), date(24, 10, 1), CityType.LOW),
        Project(date(24, 10, 2), date(24, 10, 6), CityType.HIGH),
        Project(date(24, 10, 6), date(24, 10, 9), CityType.LOW)
    ]
    assert Reimburse(projects).calculate_reimburstment() == -1

def test_set3():
    projects = [
        Project(date(24, 9, 30), date(24, 10, 3), CityType.LOW),
        Project(date(24, 10, 5), date(24, 10, 7), CityType.HIGH),
        Project(date(24, 10, 8), date(24, 10, 8), CityType.HIGH)
    ]
    assert Reimburse(projects).calculate_reimburstment() == -1

def test_set4():
    projects = [
        Project(date(24, 10, 1), date(24, 10, 1), CityType.LOW),
        Project(date(24, 10, 1), date(24, 10, 1), CityType.LOW),
        Project(date(24, 10, 2), date(24, 10, 3), CityType.HIGH),
        Project(date(24, 10, 2), date(24, 10, 6), CityType.HIGH)
    ]
    assert Reimburse(projects).calculate_reimburstment() == -1