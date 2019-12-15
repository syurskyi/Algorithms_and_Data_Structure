x = "There are %d types of people "%10  #10 means 2 in binary. here int value 10 is replaced insated of %d

binary = "binary"
do_not = "don't"

y = "Those who know %s and those who %s "%(binary, do_not) # values from the above two variables are replaced here

print x # print the replaced string 1
print y # print the replaced string 2

print "I said: %r ." %x #display the line 1 string as raw so that it is displayed with the quotes
print "I also said '%s' " %y #disply the y string marked with '%s' so that with quotes it is displayed


hilarious = False # False is a boolean value. false is not
joke_evaluation = "Isn't that the joke so funny? ! %r"
print joke_evaluation%hilarious #boolean value replaced as raw value

w = "This is the left side of..."
e = "a string with a right side."

print w + e #concatenation of two string using +
