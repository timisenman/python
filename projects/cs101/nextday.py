def nextDay(year, month, day):
    
    if day < 30: 
        day = day+1
    if month < 12 and day == 30:
        month = month+1
        day = 1
    if month == 12 and day == 30:
        year = year+1 
        day = 1 
        month = 1 
    return year, month, day
    
print nextDay(2016, 7, 17)
print nextDay(2016, 7, 30)
print nextDay(2016, 12, 30)

#Alternatively, you could solve it thusly:
def nextDay(year, month, day):
    if day < 30:
        return year, month, day+1
    else:
        if month < 12:
            return year, month+1, 1
        else: year +1, 1, 1

print nextDay(1, 1, 1)
print nextDay(2025, 12, 30)
print nextDay(2016, 7, 17)
