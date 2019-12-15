# prime and happy numbers to be read from files and find the overlapping numbers


def read_file_to_list(filename):
	file_object = open(filename)

	readlist = []
	line = file_object.readline()
	while line:
		readlist.append(int(line))
		line = file_object.readline()
	file_object.close()
	print readlist
	return readlist


def overlapping_numbers(primefile,happyfile):
	primelist = read_file_to_list(primefile)
	happylist = read_file_to_list(happyfile)
	
	return [element for element in set(primelist) if element in happylist]

if __name__=="__main__":

	primefile = "primenumbers.txt"
	happyfile = "happynumbers.txt"
	print overlapping_numbers(primefile, happyfile)
