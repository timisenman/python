# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     #add years, months, and days together    
#     #Getting years
#     if year2>year1: 
#         yearDays = (year2 - year1)*360
#         return yearDays
#     else: 
#         return yearDays = 0
#     #Getting months
#     if month2 > month1: 
#         return monthDays = (month2-month1)*30
#     else:
#         return monthDays = 0
#     #Getting days
#     if day2 < day1: 
#         return days = day2-30
#     return yearDays+monthDays+days

# print daysBetweenDates()

#define a helper function to solve this problem. 

def nextDay(year, month, day):
    if day < 30:
        return year, month, day+1
    else:
        if month < 12:
            return year, month+1, 1
        else: year +1, 1, 1

# print nextDay(1, 1, 1)
# print nextDay(2025, 12, 30)
# print nextDay(2016, 7, 17)

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
        return days

print daysBetweenDates(2012, 5, 12, 2012, 5, 15)
