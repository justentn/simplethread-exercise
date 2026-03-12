from datetime import timedelta

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

    def __init__(self, projects: list[Project]):
        """
        Initialize a set of projects used for calculations.
        
        Args:
            projects: A list of projects
        """

        self.projects = projects

    def calculate_reimburstment(self) -> int:
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
        
        # find any gaps between projects to any additional travel days.
        for i in range(len(sortedProjects) - 1):
            currentProject = sortedProjects[i]
            nextProject = sortedProjects[i + 1]

            if (nextProject.startDate - currentProject.endDate).days > 1:
                travelDates.add(currentProject.endDate)
                travelDates.add(nextProject.startDate)

        # calculate the reimbursement 
        for project in sortedProjects:
            currentProject = project.startDate
            while currentProject <= project.endDate:
                """ 
                check if we have already been reimbursed for the day

                note: if overlapping projects cover the same date, 
                the first project with the earliest start date will determine 
                the reimbursement rate for that day.
                """
                if currentProject not in seenDates:
                    seenDates.add(currentProject)
                    isTravelDay = currentProject in travelDates
                    if isTravelDay:
                        total += 55 if project.cityType == CityType.HIGH else 45
                    else:
                        total += 85 if project.cityType == CityType.HIGH else 75

                currentProject += timedelta(days=1) 

        return total
