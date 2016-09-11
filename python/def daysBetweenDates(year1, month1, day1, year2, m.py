def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    #add years, months, and days together    
    #Getting years
    if year2>year1: 
        return yearDays = (year2 - year1)*360 
    else: 
        return yearDays = 0
    #Getting months
    if month2 > month1: 
        return monthDays = (month2-month1)*30
    else:
        return monthDays = 0
    #Getting days
    if day2 < day1: 
        return days = day2-30
    return yearDays+monthDays+days