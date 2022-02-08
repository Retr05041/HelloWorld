# --<{       Counting Sundays       }>--
# --<{  Coded by Parker Cranfield   }>--
# --<{     September 02, 2020       }>--

"""
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
#=======================================================================================================================
"""
January - 31 days
February - 28 days in a common year and 29 days in leap years
March - 31 days
April - 30 days
May - 31 days
June - 30 days
July - 31 days
August - 31 days
September - 30 days
October - 31 days
November - 30 days
December - 31 days
"""

from datetime import datetime

num_of_sundays = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        date_atm = datetime(year, month, 1)
        if date_atm.strftime("%a") == "Sun":
            num_of_sundays += 1

print(num_of_sundays)
