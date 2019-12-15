from datetime import date
dt1 = date(1998,11,19)
dt2 = date(2019,3,3)
delta = dt2 - dt1
print("Kasper Grønbek is " + str(delta.days) + " days old as of this date.")