from datetime import timedelta
from typing import Final

from reimburse.citytype import CityType
from reimburse.project import Project

LOW_COST_FULL_DAY_RATE: Final[int] = 75
HIGH_COST_FULL_DAY_RATE: Final[int] = 85
LOW_COST_TRAVEL_DAY_RATE: Final[int] = 45
HIGH_COST_TRAVEL_DAY_RATE: Final[int] = 55

def calculate_reimbursement(projects: list[Project]) -> int:
    """
    Calculates the reimbursement amount.

    Args:
        projects: A list of projects

    Returns:
        The total reimbursement amount in dollars.
    """

    total = 0
    seenDates = set()

    # sort projects by their start date.
    sortedProjects = sorted(projects, key=lambda p: p.startDate)

    if not sortedProjects: 
        return 0

    travelDates = _find_gap_travel_days(sortedProjects)

    # calculate the reimbursement.
    for project in sortedProjects:
        currentProjectStartDate = project.startDate
        while currentProjectStartDate <= project.endDate:
            """ 
            check if we have already been reimbursed for the day

            note: if overlapping projects cover the same date, 
            the first project with the earliest start date will determine 
            the reimbursement rate for that day.
            """
            if currentProjectStartDate not in seenDates:
                seenDates.add(currentProjectStartDate)
                isTravelDay = currentProjectStartDate in travelDates

                if isTravelDay:
                    total += HIGH_COST_TRAVEL_DAY_RATE if project.cityType == CityType.HIGH else LOW_COST_TRAVEL_DAY_RATE
                else:
                    total += HIGH_COST_FULL_DAY_RATE if project.cityType == CityType.HIGH else LOW_COST_FULL_DAY_RATE

            currentProjectStartDate += timedelta(days=1) 

    return total


def _find_gap_travel_days(projects: list[Project]) -> set:
    """
    Finds gaps between projects and marks them as travel days.

    Args:
        projects: A list of projects 

    Returns:
        A set of travel days between projects.
    """

    travelDates = set()
    # first and last days of a project are travel days.
    travelDates.add(projects[0].startDate)
    travelDates.add(projects[-1].endDate)

    # find any gaps between projects to determine any
    # additional travel days.
    for i in range(len(projects) - 1):
        currentProject = projects[i]
        nextProject = projects[i + 1]

        if (nextProject.startDate - currentProject.endDate).days > 1:
            travelDates.add(currentProject.endDate)
            travelDates.add(nextProject.startDate)

    return travelDates

