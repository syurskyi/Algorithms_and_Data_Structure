
print 'a' and 'b'

print "b should be printed\n\n"


print '' and 'b' #null and b null will be printed

print " null should be printed\n\n"

print ' ' and 'b' #space and b , b should be printed since space is considered true

print "b should be printed since space has truth value as True\n\n"

print 'a' and 'b' and 'c'

print "c should be printed. and evaluates until the final expression if true and returns the last value else returns the first false value\n\n"


print "now we will work with or logic. expression is evaluated from left to right like and . returns first True value . else returns the last false value\n\n"

print 'a' or 'b'

print "a should be printed since a is the first true value\n\n"

print '' or 'b'

print "b should be printed since b is the first true value\n\n"

print ' ' or 'b'

print "space will be printed since space is the first true value\n\n"

print 'a' or 'b' or 'c'

print "a will be printed since a is the first true value\n\n"

print '' or {} or '' or 1 or []

print "1 will be printed since 1 is the first true value\n\n"

print '' or {} or []

print "[] will be printed since it is the last false value\n\n"

def sidefx():
	print "in sidefx"
	return 1

print 'a' or sidefx()

print " a will be printed and <in side fx> will not be printed since the function wil not be called\n\n "



a="first"
b="second"

print 1 and a or b
print "first will be printed since first 1 and a will be true and returns immediately\n\n"

print 0 and a or b
print"second will be printed since 0 and a evalutes to false and next or b gives second as value\n\n"


print "and or trick fails"
a=""
b="second"

print 1 and a or b
print " second will be printed since 1 and null returns null and null or b return second\n\n"

print "to make it work as expected use [a] [b]"

print [a]
print [b]
print 1 and [a] or [b]
