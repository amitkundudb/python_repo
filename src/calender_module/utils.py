#Finding the day of the week in a specified date
#Input containing the space separated month, day and year,
# respectively, in MM DD YYYY format.

import logging
import calendar

def get_day_of_week():
    m, d, y = map(int, input().split())
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    weekday_number = calendar.weekday(y, m, d)
    weekday_name = calendar.day_name[weekday_number]
    logging.info(weekday_name.upper())
    return weekday_name.upper()
