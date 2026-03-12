from reimburse.project import Project

"""
Class used to calculate reimbursements for projects.
"""
class Reimburse:
    """list of projects used for calculations"""
    projects = list[Project]

    """Initialize a set of projects used for calculations."""
    def __init__(self, projects: list[Project]):
        self.projects = projects

    """Calculates the reimbursement amount."""
    def calculate_reimburstment(self) -> float:
        pass
