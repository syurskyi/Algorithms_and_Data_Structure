#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import json
import os
from collections import Counter


def getFromJson():
    cwd = os.getcwd()
    filePath = cwd + '/34-birthday-json/birthdays.json'
    with open(filePath, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    birthdays = getFromJson()
    values = list(birthdays.values())
    months = []
    for date in values:
        month = (date.split('.'))[1]
        months.append(month)

    yearMonths = {
        '01': 'January',
        '02': 'Februrary',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }

    count = Counter(months)
    for key in count.keys():
        print('In {} were {} guys'.format(yearMonths[key], count[key]))
