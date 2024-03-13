#Finding the day of the week in a specified date
#Input containing the space separated month, day and year,
# respectively, in MM DD YYYY format.

import logging
import calendar

def get_day_of_week(year, month, day):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    weekday_number = calendar.weekday(year, month, day)
    weekday_name = calendar.day_name[weekday_number]
    logging.info(weekday_name.upper())

# Taking user input
m, d, y = map(int, input().split())
