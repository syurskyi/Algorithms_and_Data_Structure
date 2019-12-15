#! /Users/piotrjankiewicz/anaconda3/bin/python3.6

def grid(w, h):
    for i in range(h):
        print(' --- ' * w)
        print('|    ' * w + '|' )
    print(' --- ' * w )


if __name__ == '__main__':
    width = int(input("Grid's width: "))
    height = int(input("Grid's height: "))
    grid(width, height)
