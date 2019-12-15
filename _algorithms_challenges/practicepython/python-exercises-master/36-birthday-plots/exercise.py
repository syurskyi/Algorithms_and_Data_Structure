#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import json
import os
from collections import Counter

from bokeh.plotting import figure, show, output_file

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


def getFromJson():
    cwd = os.getcwd()
    filePath = cwd + '/34-birthday-json/birthdays.json'
    with open(filePath, 'r') as file:
        return json.load(file)


def formatDataToStringMonths(values):
    months = []
    for date in values:
        month = (date.split('.'))[1]
        months.append(month)

    count = Counter(months)
    print(count)
    result = {}
    for key in count.keys():
        result[yearMonths[key]] = count[key]

    return result


def printPlot(data):
    output_file("plot.html")
    x_categories = list(yearMonths.values())
    x = list(data.keys())
    y = list(data.values())
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)
    show(p)

if __name__ == "__main__":
    birthdays = getFromJson()
    values = list(birthdays.values())
    data = formatDataToStringMonths(values)
    printPlot(data)
