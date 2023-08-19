# https://py.checkio.org/en/mission/when-is-friday/

import datetime

def friday(d):
    date_object = datetime.datetime.strptime(d, "%d.%m.%Y")
    day_of_week = date_object.weekday()
    w = 0
    
    if day_of_week <= 4:
        w = 4 - day_of_week
    else:
        w = 11 - day_of_week
        
    return w

assert friday("12.04.2018") == 1
assert friday("01.01.1999") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")


