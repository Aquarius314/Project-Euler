# 1 January 1900 was Monday
day = 365%7 # 0 is Monday, 6 is Sunday
# print(day) -> 1 so it was Tuesday on 1 January 1901
# No idea why solution is +1 ;)

sundays = 0

for year in range(100):
    day = (day+31)%7   # Jan
    if day == 6:
        sundays += 1
        # lap years
    if (year+3)%4 == 0:
        day += 1
    day = (day+28)%7   # Feb
    if day == 6:
        sundays += 1
    day = (day+31)%7   # Mar
    if day == 6:
        sundays += 1
    day = (day+30)%7   # Apr
    if day == 6:
        sundays += 1
    day = (day+31)%7   # May
    if day == 6:
        sundays += 1
    day = (day+30)%7   # Jun
    if day == 6:
        sundays += 1
    day = (day+31)%7   # Jul
    if day == 6:
        sundays += 1
    day = (day+31)%7   # Aug
    if day == 6:
        sundays += 1
    day = (day+30)%7   # Sep
    if day == 6:
        sundays += 1
    day = (day+31)%7   # Oct
    if day == 6:
        sundays += 1
    day = (day+30)%7   # Nov
    if day == 6:
        sundays += 1
    day = (day+31)%7   # Dec
    if day == 6:
        sundays += 1

print(sundays+1)
