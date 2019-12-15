formatter = "%r %r %r %r "
print formatter % (1,2,3,4)
print formatter % ("one", "two" , "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

print formatter %(
    "I had this thing.",
    "That you could type right",
    "But it didn't sing",   #since the word didnt has apostrope ' character it is printed inside double quotes
    "so i said good night"
    )
