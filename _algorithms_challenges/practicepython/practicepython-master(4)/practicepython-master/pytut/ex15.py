

from sys import argv

script, filename = argv

txt_in_file =  open(filename)

print txt_in_file.read()

print "open another file"

filename_new = raw_input("Type the new file to be opened")

txt_in_file_new = open(filename_new)

print "txt_in_file_new %s"%txt_in_file_new.read()

lines = txt_in_file_new.readline()
while lines:
    print i
    lines = txt_in_file_new.readline()
