from os.path import exists
from sys import argv

script, from_file, to_file = argv
#this script will copy a file content into anoter file

in_file = open(from_file)
in_data = in_file.read()
print "The input file is %d bytes long "%len(in_data)
print "check whether the output file exist %r"%exists(to_file)
print "press Ctrl c to exit Return to continue"
raw_input()
out_file = open(to_file,'w')
out_file.write(in_data)
print "Done"

in_file.close()
out_file.close()
