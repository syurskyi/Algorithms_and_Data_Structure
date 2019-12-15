import calendar
c_year, c_month = int(input("Write the year, you want the calendar from: ")), int(input("Write the number of the month you want the calendar from: "))
print(calendar.month(c_year, c_month))