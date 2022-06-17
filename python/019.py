"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

# two approaches..   first a dumb


def isYearLeap(year):
  return True if (year%4==0) & (year%100!=0 | year%400==0) else False

# get how many days are in a month 
def getDaysInMonth(month, year):
  if month in [1,3,5,7,8,10,12]:
    return 31
  elif month in [4,6,9,11]:
    return 30 
  elif month == 2:
    return 29 if isYearLeap(year) else 28
  raise Exception("invalid month")



# this code is a bit messy, the conditions are hardcoded.  Could be generalized. 
sun_count = 0

day = 1
for y in range(1900, 2001):
  for m in range (1, 13):
    if (day == 0) & (y>1900):
      sun_count += 1
    daysinmonth = getDaysInMonth(m,y)
    #print("y/m/days in month/d",y,m,daysinmonth,day, dname[day])
    day = (day + daysinmonth) % 7 

print(sun_count)


