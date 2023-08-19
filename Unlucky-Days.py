# https://py.checkio.org/en/mission/unlucky-days/

import datetime

def checkio(y):
    w = 0
    i = 1
    
    while i < 13:
        day_of_week = datetime.date(y, i, 1).weekday()
        
        if day_of_week == 6:
            w += 1
            
        i += 1
        
    return w


if __name__ == "__main__":
    print("Example:")
    print(checkio(2015))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
    print("Coding complete? Click 'Check' to earn cool rewards!")

