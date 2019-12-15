ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait theres not 10 things in that list, lets fix that"

stuff = ten_things.split()

print stuff

more_stuff = ["Day" , "night", "song", "frisbee", "corn", "banana", "Girl", "boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding",next_one
    stuff.append(next_one)
    print "There are %d items now"%len(stuff)

print "There we go: ",stuff
print "Lets do somethings with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
