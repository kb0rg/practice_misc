import datetime
import calendar

WEEKDAYS = {day: num for (num, day) in enumerate(calendar.day_name)}

INDEX = {
    '1st': '0',
    '2nd': '1',
    '3rd': '2',
    '4th': '3',
    '5th': '4',
    'last': '-1',
}

def meetup_day(year, month, day_of_the_week, which):
    """
    year: int: YYYY
    month: int: M or MM
    day_of_the_week: str: weekday name
    which: str: (one of: '1st', '2nd', '3rd', '4th', '5th', 'last', 'teenth')
    returns datetime.date or Exception
    """
    month_days = calendar.Calendar().itermonthdays2(year, month)
    opts = [x[0] for x in month_days if x[1] == WEEKDAYS[day_of_the_week] and x[0] != 0]

    i = INDEX.get(which)

    if not i: # is teenth
        for y in opts:
            if y > 12 and y < 20:
                day = y
                continue
    else:
        try:
            day = opts[int(i)]
        except KeyError:
            raise Exception

    return datetime.date(year, month, day)
