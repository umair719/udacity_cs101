__author__ = 'Umair'
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if (year2 - year1) > 0:
        if (year2 - year1) == 1 and month1 > month2:
            days += 0
        else:
            for x in range(year1, year2):
                if isLeapYear(x):
                    days += 366
                else:
                    days += 365
    if (abs(month2 - month1)) > 0:
        if month2 < month1:
            for x in range(0, month2):
                days += daysOfMonths[x]
            for x in range(month1 - 1, 11):
                days += daysOfMonths[x]
        else:
            for x in range(month1, month2):
                days += daysOfMonths[x - 1]
    if day2 == daysOfMonths[month2 - 1] and day1 != day2:
        days += day2 - day1
    else:
        days += 1 if (day2 - day1) == 0 else abs((day2 - day1) + 1)
    return days


def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Test routine

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585 ),
                  ((1900, 1, 1, 1999, 12, 31), 36523),
                  ((2012, 10, 2, 2013, 3, 2), 152)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed - Result returned: ", result, "Expected: ", answer)
        else:
            print("Test case passed!")


test()
