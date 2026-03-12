from datetime import date

from reimburse.citytype import CityType

"""
An object representing a project. Defines start dates and end dates.

First and last days are considered travel dates.
"""
class Project: 
    """Start date."""
    startDate = date

    """End date."""
    endDate = date

    """
    Determines if this project is located within a high cost
    or low cost city.
    """
    cityType = CityType
    
    def __init__(self, start: date, end: date, cityType: CityType):
        self.startDate = start
        self.endDate = end
        self.cityType = cityType
