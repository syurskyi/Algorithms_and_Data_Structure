import datetime
import sys

def main():
	sundays = []
	curr_date = datetime.date(1901, 1, 1)
	while curr_date <= datetime.date(2000, 12, 31):
		if curr_date.day is 1 and curr_date.weekday() is 6:
			sundays += [curr_date]
		curr_date += datetime.timedelta(days=1)
	print(len(sundays))
	
if __name__ == '__main__':
    sys.exit(main())
