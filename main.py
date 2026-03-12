#!/usr/bin/python3

from datetime import date

from reimburse.citytype import CityType
from reimburse.project import Project
from reimburse.reimburse import Reimburse


if __name__ == "__main__":
    set1 = [
        Project(date(2024, 10, 1), date(2024, 10, 4), CityType.LOW),
    ]

    set2 = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 2), date(2024, 10, 6), CityType.HIGH),
        Project(date(2024, 10, 6), date(2024, 10, 9), CityType.LOW),
    ]

    set3 = [
        Project(date(2024, 9, 30), date(2024, 10, 3), CityType.LOW),
        Project(date(2024, 10, 5), date(2024, 10, 7), CityType.HIGH),
        Project(date(2024, 10, 8), date(2024, 10, 8), CityType.HIGH),
    ]

    set4 = [
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 1), date(2024, 10, 1), CityType.LOW),
        Project(date(2024, 10, 2), date(2024, 10, 3), CityType.HIGH),
        Project(date(2024, 10, 4), date(2024, 10, 6), CityType.HIGH),
    ]

    print(f"Set 1: ${Reimburse(set1).calculate_reimburstment()}")
    print(f"Set 2: ${Reimburse(set2).calculate_reimburstment()}")
    print(f"Set 3: ${Reimburse(set3).calculate_reimburstment()}")
    print(f"Set 4: ${Reimburse(set4).calculate_reimburstment()}")
