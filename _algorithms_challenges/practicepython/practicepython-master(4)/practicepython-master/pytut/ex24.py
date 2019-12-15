print "Lets practice everything"

print "You'd need to know   \'about escapes with \\ that do \n newlines and \t tabs"


poem = """
\t The lovely world with logic so firmly planted
cannot discern \n the needs of love
nor comprehend the passion from itution
and requires an explanation
\n\t\twhere there is none.
"""

print "---------------"
print poem
print "---------------"


five = 10 - 2 + 3 - 6
print "This should be five %d"%five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans , jars, crates = secret_formula(start_point)


print "with a starting point of %d" % start_point
print "WE'd have had %d beans, %d jars and %d crates "%(beans,jars,crates)

start_point = start_point /10
print "we have also done this way"
print "WE'd have had %d beans, %d jars and %d crates "%secret_formula(start_point)
