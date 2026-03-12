from datetime import date

"""
An object representing a project. Defines start dates and end dates.

First and last days are considered travel dates.
"""
class Project: 
    # Start Date
    startDate = date()
    # End Date
    endDate = date()
    # Flag to determine if this project rates belong in a low cost or high cost city
    isLowCost = False
    
    def __init__(self, start, end, isLowCost):
        self.startDate = start
        self.endDate = end
        self.isLowCost = isLowCost
