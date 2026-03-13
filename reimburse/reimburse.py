from datetime import timedelta
from typing import Final

from reimburse.citytype import CityType
from reimburse.project import Project

# reimbursement rates in dollars
LOW_COST_FULL_DAY_RATE: Final[int] = 75    # full day in a low cost city
HIGH_COST_FULL_DAY_RATE: Final[int] = 85   # full day in a high cost city
LOW_COST_TRAVEL_DAY_RATE: Final[int] = 45  # travel day in a low cost city
HIGH_COST_TRAVEL_DAY_RATE: Final[int] = 55 # travel day in a high cost city

def calculate_reimbursement(projects: list[Project]) -> int:
    """Calculates the reimbursement amount.

    Args:
        projects: A list of projects.

    Returns:
        The total reimbursement amount in dollars.
    """

    total = 0
    seen_dates = set()

    # sort projects by their start date.
    sorted_projects = sorted(projects, key=lambda p: p.start_date)

    if not sorted_projects: 
        return 0

    travel_dates = _find_gap_travel_days(sorted_projects)

    # calculate the reimbursement.
    for project in sorted_projects:
        current_date = project.start_date
        while current_date <= project.end_date:
            # check if we have already been reimbursed for the day
            # note: if overlapping projects cover the same date, 
            # the first project in the list with the date will determine 
            # the reimbursement rate for that day.
            if current_date not in seen_dates:
                seen_dates.add(current_date)
                is_travel_day = current_date in travel_dates
                total += _get_rate(project.city_type, is_travel_day)

            current_date += timedelta(days=1) 

    return total

def _find_gap_travel_days(projects: list[Project]) -> set:
    """Finds gaps between projects and marks them as travel days.

    Args:
        projects: A list of projects.

    Returns:
        A set containing travel dates.
    """

    travel_dates = set()
    # grab the first travel date
    travel_dates.add(projects[0].start_date)
    # grab the latest end date
    travel_dates.add(max(p.end_date for p in projects))

    # find any gaps between projects to determine any
    # additional travel days.
    for i in range(len(projects) - 1):
        current_project = projects[i]
        next_project = projects[i + 1]

        # 0 = overlap, 1 = contiguous, >1 = gap
        if (next_project.start_date - current_project.end_date).days > 1:
            travel_dates.add(current_project.end_date)
            travel_dates.add(next_project.start_date)

    return travel_dates

def _get_rate(city_type: CityType, is_travel_day: bool) -> int:
    """Gets the reimbursement rate for a given city type (low or high cost) 
    and day type (travel or full day).

    Args:
        city_type: Type of city.
        is_travel_day: Whether the day is a travel day.

    Returns:
        The reimbursement rate in dollars.
    """
    
    rate = 0
    
    if city_type == CityType.HIGH:
        rate = (
            HIGH_COST_TRAVEL_DAY_RATE
            if is_travel_day 
            else HIGH_COST_FULL_DAY_RATE
        )
    else:
        rate = (
            LOW_COST_TRAVEL_DAY_RATE 
            if is_travel_day 
            else LOW_COST_FULL_DAY_RATE
        ) 

    return rate
