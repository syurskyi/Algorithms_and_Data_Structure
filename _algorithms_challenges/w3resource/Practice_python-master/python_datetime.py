import datetime
import calendar
import time


# 1
def display_time():
    """ Displays date and time from the date and time now."""
    now = datetime.datetime.now()
    date_time = now.strftime("date: %b/%d/%Y, time: %I:%M %p")
    print(date_time)
    print("\n------------------------------------------------------\n")
    print(now.strftime("year: %Y"))
    print(now.strftime("month: %B"))
    print(now.strftime("week number of the year: %U"))
    print(now.strftime("Weekday of the week: %w"))
    print(now.strftime("Day of the year: %j"))
    print(now.strftime("Day of the month: %d"))
    print(now.strftime("Day of the week: %A"))

# display_time()


# 2
def leapyear_checker(year):
    """ Checks if given year is a leap year. """
    if calendar.isleap(year):
        print("{} is a leap year.".format(year))
        return True
    else:
        print("{} is not a leap year.".format(year))
        return False

# leapyear_checker(2015)


# 3
def make_datetime():
    """ makes a datetime from a given date and time with strptime """
    date = input("Please give a date as month/day/year, (month ex jan feb): ")
    time = input("Please give a time in hour:minute (AM/PM):  ")
    the_datetime = date + time
    try:
        our_datetime = datetime.datetime.strptime(the_datetime, "%b/%d/%Y%I:%M %p")
        return our_datetime
    except ValueError:
        return make_datetime()

# print(make_datetime())


# 4
def time_now():
    """Return the time at current time. """
    return datetime.datetime.now().time()

# print(time_now())


# 5
def five_days_before(date=datetime.datetime.now().date()):
    five_days_ago = date - datetime.timedelta(5)
    five_days_ago = five_days_ago.strftime("%b/%d/%Y")
    print("5 days before current date:    {}".format(five_days_ago))

# five_days_before()


# 6
# unix_timestamp is the amount of seconds passed since 1970
# 1459141485 is the unix timestamp of Mar/28/2016    1:04:05 AM
def unix_timestamp_date(unix=1459141485):
    """ converts a given unix timestamp into readable time."""
    return datetime.datetime.fromtimestamp(int(unix))

# print(unix_timestamp_date("1459141485"))


# 7
def today_yesterday_tommorow(today=datetime.datetime.now().date()):
    """ Tells you the date of today and the day tommorow and yesterday """
    print("today: {}".format(today))
    yesterday = today - datetime.timedelta(1)
    tommorow = today + datetime.timedelta(1)
    print("yesterday: {}".format(yesterday.strftime("%d")))
    print("tommorow: {}".format(tommorow.strftime("%d")))

# today_yesterday_tommorow()


# 8
def date_datetime():
    """ returns a datetime from a given date """
    date = input("give date in mon/day/year format(month like jan feb): ")
    return datetime.datetime.strptime(date, "%b/%d/%Y")

# print(date_datetime())


# 9
def next_5_days(today=datetime.datetime.now().date()):
    """ returns the next 5 days after current """
    print("today: {}".format(today))
    for num in range(1, 6):
        print("{} day: {}".format(num, today + datetime.timedelta(num)))

# next_5_days()


# 10
def add_5_seconds(time=datetime.datetime.now()):
    """ Adds 5 seconds to the current time """
    print(time.time())
    print((time + datetime.timedelta(0, 5)).time())

# add_5_seconds()


# 11
def day_of_year(date=datetime.datetime.now()):
    """ returns the day of the year from a datetime """
    return date.strftime("Its the %j day of %Y'th year.")

# print(day_of_year())


# 12
def millisecond():
    """returns the given millisecond of the day by timesing second by 1000 """
    return int(round(time.time() * 1000))

# print(millisecond())


# 13
def current_week_number(date=datetime.datetime.now()):
    """ returns the current week number (week of the year starting from monday)
    of a given date or current date
    """
    return int(date.strftime("%W"))

# print(current_week_number())


# 14 3
def first_monday_of_week(year, week):
    """ returns the date of the first monday of a given week of a given year"""
    weekyear = "{} {} 1".format(year, week)
    return time.asctime(time.strptime(weekyear, "%Y %U %w"))

print(first_monday_of_week(2015, 50))


# 15
def sundays_of_year(year):
    first_week = "{} 1 0".format(year)
    first_week = time.asctime(time.strptime(weekyear, "%Y %U %w"))
    sunday = int(first_week.strftime("%j"))
    # while sunday < 366:


# 16
def add_years(date, add):
    date = datetime.date(date)
    year = date.year
    
