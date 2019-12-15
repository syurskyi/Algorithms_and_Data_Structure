the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this is first kind of for-loop goess through the list
for number in the_count:
    print "this is count %d "%number


#same as above

for fruit in fruits:
    print "this is fruit %s " %fruit

#also we can go through a mixed list. since we dont know type use %r for formatting

for i in change:
    print "I got %r"%i


#we can also build lists. first start with an empty one

elements = []
#then use range function to do 0 to 5 counts
for i in range(0,6):
    print "adding %d to the list"%i
    elements.append(i)

#now we can print them too
for i in elements:
    print "elements was %d"%i
