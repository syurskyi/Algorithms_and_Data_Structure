# !/usr/bin/env python
import datetime

if __name__ == "__main__":
    age = (int(raw_input('Please enter your age:')))
    name = (str(raw_input('Please enter your name:')))
    year = (int(raw_input('Please enter the current year:')))

    statement = ('\n' + name + ', You will be 100 years old in ' + str(year - age + 100))

    print(statement)
    # print('I run myself\n')
    # name = str(input('Give me your name: '))
    # print('Your name is ' + name)
    # age = int(input("Give me your age: "))
    # print('Your are ' + age + ' years old\n')
    # yearsTill100 = 100 - age
    # now = datetime.datetime.now()
    # finalYear = now.year + yearsTill100
    # print('You will be 100 in ' + finalYear)
else:

    print('I am being imported')
