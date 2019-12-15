d = {"server":"mpilgrim", "database":"master"}
print d

print "print all the methods associated with dict"
print dir(d)
print type(d)

print d["server"]
print d["database"]
#print d["mpilgrim"] # error coz of no key present


print "\n#modify value for key database value by reassigning -- this already exists\n"
d["database"]="pub"
print d

print "\n#add new key\n"
d["pravnkey"] = "praveenValue"
print d

#remember order is not maintained in dictionary
#keys are case sensitive

print "\n# can have any type mixed\n"
d["retryCount"] = 3
d[42] = "douglas"
print d


print "\n#del key is used to delete a key from the dict. clear() to clear all elements\n"

print "\n deleting 42 key element"
del d[42]
print d

print "\ndeleting all element using clear()"
d.clear()
print d
