from datetime import timedelta
from typing import Final

from reimburse.citytype import CityType
from reimburse.project import Project


class Reimburse:
    """
    Class used to calculate reimbursements for projects.

    Contains a list of projects used for reimbursements. Reimbursements are 
    determined based on if the dates fall on a travel day or a full day.

    Full day rates
        High cost city: 85
        Low cost city: 75
    Travel day rates
        High cost city: 55
        Low cost city: 45
    """

    projects: list[Project] = []
    LOW_COST_FULL_DAY_RATE: Final[int] = 75
    HIGH_COST_FULL_DAY_RATE: Final[int] = 85
    LOW_COST_TRAVEL_DAY_RATE: Final[int] = 45
    HIGH_COST_TRAVEL_DAY_RATE: Final[int] = 55

    def __init__(self, projects: list[Project]):
        """
        Initialize a set of projects used for calculations.
        
        Args:
            projects: A list of projects
        """

        self.projects = projects

    def calculate_reimbursement(self) -> int:
        """
        Calculates the reimbursement amount.

        Returns:
            The total reimbursement amount in dollars.
        """

        total = 0
        travelDates = set()
        seenDates = set()

        # sort projects by their start date.
        sortedProjects = sorted(self.projects, key=lambda p: p.startDate)

        if not sortedProjects: 
            return 0

        # first and last days of a project are travel days.
        travelDates.add(sortedProjects[0].startDate)
        travelDates.add(sortedProjects[-1].endDate)
        
        # find any gaps between projects to determine any
        # additional travel days.
        for i in range(len(sortedProjects) - 1):
            currentProject = sortedProjects[i]
            nextProject = sortedProjects[i + 1]

            if (nextProject.startDate - currentProject.endDate).days > 1:
                travelDates.add(currentProject.endDate)
                travelDates.add(nextProject.startDate)

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
                        total += self.HIGH_COST_TRAVEL_DAY_RATE if project.cityType == CityType.HIGH else self.LOW_COST_TRAVEL_DAY_RATE
                    else:
                        total += self.HIGH_COST_FULL_DAY_RATE if project.cityType == CityType.HIGH else self.LOW_COST_FULL_DAY_RATE

                currentProjectStartDate += timedelta(days=1) 

        return total
