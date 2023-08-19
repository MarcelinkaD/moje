# https://py.checkio.org/en/mission/weekend-counter/

from datetime import datetime, timedelta, date


def checkio(from_date, to_date):
    weekend_count = 0
    current_date = from_date

    while current_date <= to_date:
        if current_date.weekday() in [5, 6]: 
            weekend_count += 1
        current_date += timedelta(days=1)

    return weekend_count


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"


