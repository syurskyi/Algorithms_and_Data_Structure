

#this is multi value argument passing

def print_two(*args):
    arg1,arg2=args
    print "printing from function 1"
    print "Arg1 %r, Arg2 %r"%(arg1,arg2)


#okay now going to print the above same with different argument fromat

def print_two_again(arg1,arg2):
    print "printing from function 2"
    print "arg1 %r, arg2 %r" %(arg1,arg2)

#this one takes one argument only

def print_one(arg1):
    print "printing from fun 3"
    print "arg1 %r"%arg1

#this prints nothing
def print_nothing():
    print "I dont have anything to print"

print_two("praveen","surendran")
print_two_again("PRAVEEN","SURENDRAN")
print_one("I am praveen")
print_nothing()
