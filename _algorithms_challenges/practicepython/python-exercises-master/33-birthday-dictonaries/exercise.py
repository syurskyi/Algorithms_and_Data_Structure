#! /Users/piotrjankiewicz/anaconda3/bin/python3.6

birtdays = {
    'piotr' : '11.02.1997',
    'einstein' : '14.03.1879'
}

if __name__ == "__main__":
    print('We know birthdays of: ' + str(list(birtdays.keys())))
    name = str(input("Who's  birthday you want to know ?"))
    print('This guy birthday is ' + birtdays.get(name, ' ---  No such guy ---'))
