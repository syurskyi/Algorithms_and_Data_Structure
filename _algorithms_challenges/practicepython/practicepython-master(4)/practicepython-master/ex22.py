count = 0	
with open('nameslist.txt', 'r') as open_file:
  	line = open_file.readline()
  	while line:
    		print line
		count+=1
    		line = open_file.readline()


print "there are total %d image names " % count
