from datetime import date, datetime, timedelta
import calendar


def months_days(current_year):
    first_dates = [first_day(str(current_year) + "-" + str(i + 1) + "-" + str(1)) for i in range(12)]
    last_dates = [datetime(first_date.year, first_date.month, calendar.mdays[first_date.month])
                  for first_date in first_dates]
    year_months = [last_date.strftime("%B") for last_date in last_dates]

    months = [{year_months[i]: {"first_date": first_dates[i], "last_date": last_dates[i]}} for i in range(len(year_months))]

    return months


def first_day(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()


def str_to_date(str_date):
    new_string = str_date.replace(' ', '-').replace(',', '')
    return datetime.strptime(new_string, '%d-%B-%Y')


def last_day_of_previous_month(dt):
    return datetime(dt.year, dt.month, 1) - timedelta(days=1)


def last_day_of_current_month():
    c_date = date.today()
    start_date = datetime(c_date.year, c_date.month, 1)
    end_date = datetime(c_date.year, c_date.month, calendar.mdays[c_date.month])
    print start_date, end_date


def first_day_of_current_month(dt):
    return date(dt.year, dt.month, 1)


if __name__ == "__main__":
    print months_days(2016)
    print str_to_date('10 October, 2016')
