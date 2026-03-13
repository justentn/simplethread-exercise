# simplethread-exercise

## Technical Exercise

You have a set of projects, and you need to calculate a reimbursement amount for the set. Each project has a start date and an end date. The first day of a project and the last day of a project are considered "travel" days. Days with no travel in the middle of a project are "full" days. There are also two types of cities a project can be in, high cost cities and low cost cities.

A few rules:

    Any given day is only ever reimbursed once, even if multiple projects are on the same day.
    Projects that are contiguous or overlap, with no gap between the end of one and the start of the next, are considered a sequence of projects and should be treated similar to a single project.
    First day and last day of a project (or sequence of projects) are travel days.
    Any day in the middle of a project (or sequence of projects) is considered a full day.
    If there is a gap between projects, those gap days are not reimbursed and the days on either side of that gap are travel days.
    A travel day is reimbursed at a rate of 45 dollars per day in a low cost city.
    A travel day is reimbursed at a rate of 55 dollars per day in a high cost city.
    A full day is reimbursed at a rate of 75 dollars per day in a low cost city.
    A full day is reimbursed at a rate of 85 dollars per day in a high cost city.
    Given the following sets of projects, provide code that will calculate the reimbursement for each.


Set 1:
  Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/4/24

Set 2:
  Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/1/24

  Project 2: High Cost City Start Date: 10/2/24 End Date: 10/6/24

  Project 3: Low Cost City Start Date: 10/6/24 End Date: 10/9/24

Set 3:
  Project 1: Low Cost City Start Date: 9/30/24 End Date: 10/3/24

  Project 2: High Cost City Start Date: 10/5/24 End Date: 10/7/24

  Project 3: High Cost City Start Date: 10/8/24 End Date: 10/8/24

Set 4:
  Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/1/24

  Project 2: Low Cost City Start Date: 10/1/24 End Date: 10/1/24

  Project 3: High Cost City Start Date: 10/2/24 End Date: 10/3/24

  Project 4: High Cost City Start Date: 10/2/24 End Date: 10/6/24


## Assumptions

- When a project overlaps on the same date, the project with the earliest start date
  determines the reimbursement rate for that day.
- A project with an end date before its start date results in $0 total.
- An empty set of projects returns $0.

## Dependencies

- `Python3.11+`

## How To Run

1. Open a terminal
2. Create a python virtual environment using `python3 -m venv .venv` 
3. Activate your python virtual environment using `source .venv/bin/activate`
4. Install the required dependencies using `pip install -r requirements.txt`
5. Run the command `python3 main.py` or `pytest -s -v` 