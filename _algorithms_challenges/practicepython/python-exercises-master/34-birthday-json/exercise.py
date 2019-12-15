#! /Users/piotrjankiewicz/anaconda3/bin/python3.6
import json
import sys
import os


def getFromJson():
    cwd = os.getcwd()
    filePath = cwd + '/34-birthday-json/birthdays.json'
    with open(filePath, 'r') as file:
        return json.load(file)


def addToJson(dict):
    cwd = os.getcwd()
    filePath = cwd + '/34-birthday-json/birthdays.json'
    with open(filePath, 'r') as file:
        decoded = json.load(file)
        decoded.update(dict)
        with open(filePath, 'w') as json_file:
            json.dump(decoded, json_file)



if __name__ == "__main__":
    birthdays = getFromJson()
    print('We know birthdays of: ' + str(list(birthdays.keys())))
    name = str(input("Who's  birthday you want to know ?"))
    print('This guy birthday is ' + birthdays.get(name, ' ---  No such guy ---'))
    newName = input('Add guy to dictionary: ')
    newDate = input('And his birthday: ')
    addToJson({newName: newDate})
