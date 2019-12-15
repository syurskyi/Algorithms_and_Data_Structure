# File Overlap


def filetointeger(filename):
    integerlist = []
    with open(filename) as file:
        line = file.readline()
        while line:
            print(line)
            line = file.readline()
    return integerlist


primelist = filetointeger("primenumbers.txt")
happylist = filetointeger("happynumbers.txt")
overlaplist = [i for i in primelist if i in happylist]

print overlaplist
