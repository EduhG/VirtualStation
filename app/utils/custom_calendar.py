from datetime import date, datetime, timedelta
import calendar


def months_days():
    month_days = []

    pass

    return month_days


def last_day_of_previous_month(dt):
    return datetime(dt.year, dt.month, 1) - timedelta(days=1)


def last_day_of_current_month():
    c_date = date.today()
    start_date = datetime(c_date.year, c_date.month, 1)
    end_date = datetime(c_date.year, c_date.month, calendar.mdays[c_date.month])
    print start_date, end_date


def first_day_of_current_month(dt):
    return date(dt.year, dt.month, 1)
