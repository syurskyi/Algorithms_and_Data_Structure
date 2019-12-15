from sys import argv

script, filename = argv

print "Now we are going to erase contents of %r"%filename
print "If you dont want to erase hit CTRL+C "
print "If you want that hit RETURN"

raw_input("?")

print "Opening the file..."
target = open (filename,'w')

print "Truncating the file(Erasing its previous contents). Good bye..."
target.truncate()

print "Now I am going to ask you three lines "

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "And now I am going to write these lines to the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "And finally closing the file\n"
target.close()

target=open(filename)
print "The file contents are going to be printed"
content = target.read()
print content
