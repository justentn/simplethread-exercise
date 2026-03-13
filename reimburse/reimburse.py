from datetime import date, timedelta
from typing import Final

from reimburse.citytype import CityType
from reimburse.project import Project

# reimbursement rates in dollars
LOW_COST_FULL_DAY_RATE: Final[int] = 75    # full day in a low cost city
HIGH_COST_FULL_DAY_RATE: Final[int] = 85   # full day in a high cost city
LOW_COST_TRAVEL_DAY_RATE: Final[int] = 45  # travel day in a low cost city
HIGH_COST_TRAVEL_DAY_RATE: Final[int] = 55  # travel day in a high cost city


def calculate_reimbursement(projects: list[Project]) -> int:
    """Calculates the reimbursement amount.

    Args:
        projects: A list of projects.

    Returns:
        The total reimbursement amount in dollars.
    """

    if not projects:
        return 0

    total = 0
    seen_dates = set()
    travel_dates = _find_travel_days(projects)

    # sort projects by their start date and their city type.
    # note: sort is done to prefer high cost cities to be processed
    # first.
    sorted_projects = sorted(projects, key=lambda p: (
        p.city_type != CityType.HIGH, p.start_date))

    # calculate the reimbursement.
    for project in sorted_projects:
        current_date = project.start_date
        while current_date <= project.end_date:
            # check if we have already been reimbursed for the day
            # note: if overlapping projects cover the same date,
            # the first project in the list that claims the date will determine
            # the reimbursement rate for that day. Projects are sorted
            # based on city types to ensure the high cost rate is used.
            if current_date not in seen_dates:
                seen_dates.add(current_date)
                is_travel_day = current_date in travel_dates
                rate = _get_rate(project.city_type, is_travel_day)
                total += rate

            current_date += timedelta(days=1)

    return total


def _find_travel_days(projects: list[Project]) -> set[date]:
    """Finds gaps between projects and marks them as travel days.

    Args:
        projects: A list of projects.

    Returns:
        A set containing travel dates.
    """

    if not projects:
        return set()

    travel_dates = set()

    # filter out invalid projects where end_date is before start_date.
    valid_projects = [p for p in projects if p.start_date <= p.end_date]

    if not valid_projects:
        return set()

    date_sorted_projects = sorted(valid_projects, key=lambda p: p.start_date)
    first_start_date = date_sorted_projects[0].start_date
    last_end_date = max(p.end_date for p in date_sorted_projects)

    # throw in the very first day and latest date into our
    # travel day bucket
    travel_dates.add(first_start_date)
    travel_dates.add(last_end_date)

    # find any gaps between projects to determine any
    # additional travel days.
    rolling_max_end_date = date_sorted_projects[0].end_date
    for i in range(len(date_sorted_projects) - 1):
        # keep a rolling max to make sure we do not
        # capture false gaps
        rolling_max_end_date = max(
            rolling_max_end_date, date_sorted_projects[i].end_date)
        next_project = date_sorted_projects[i + 1]

        # 0 = overlap, 1 = contiguous, >1 = gap
        if (next_project.start_date - rolling_max_end_date).days > 1:
            travel_dates.add(rolling_max_end_date)
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
