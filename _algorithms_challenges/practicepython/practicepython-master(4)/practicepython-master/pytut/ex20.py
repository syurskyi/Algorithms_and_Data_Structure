from sys import argv

#read from command line arguments
script , input_file = argv

#print all the contents of the file
def print_all(f):
    print f.read()


#print the reverse of a file
def rewind(f):
    f.seek(0)

#print a line
def print_a_line(line_count, f):
    print line_count,f.readline()

current_file =  open(input_file)

print "Lets print the whole file\n"
print_all(current_file)

print "Now lets rewind the file like  a tape\n"
rewind(current_file)

print "Lets print three lines\n"
current_line = 1

print_a_line(current_line, current_file)

current_line = current_line + 1

print_a_line(current_line, current_file)

current_line+=1
print_a_line(current_line, current_file)
