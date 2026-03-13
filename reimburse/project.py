from datetime import date

from reimburse.citytype import CityType


class Project:
    """An object representing a project. 

    A project contains information on the project's start and end dates and
    if it resides in a low cost or high cost city.
    """

    start_date: date
    end_date: date
    city_type: CityType

    def __init__(self, start: date, end: date, city_type: CityType):
        """Initializes a project with a start date, end date and a city type.

        Args:
            start: The project's start date.
            end: The project's end date.
            city_type: Determines if the project is in a high or low cost city.
        """

        self.start_date = start
        self.end_date = end
        self.city_type = city_type
