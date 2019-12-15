# birthday dictionary to get a persons birhday by entering their name


def name_look_dictionary():
	bday_dict = dict()
	with open("birthday_dictionary.txt") as file_object:
		line = file_object.readline()
		while line:
			text = line.strip()
			#print text
			name_dob = text.split("=")
			
			bday_dict[name_dob[0].strip()] = name_dob[1].strip() 
			line = file_object.readline()
	return bday_dict

def user_interaction_birthday_find(bday_dict):
	print "Welcome to birthday Dictionary"
	print "I have birthdays of the below persons"
	
	for k,v in bday_dict.items():
		print k

	name = raw_input("Enter the name of person whose birthday I will reveal> ")
	
	print "You have asked for %s's birthday" % name
	if name in bday_dict:
		print "The birthday is on %s "% bday_dict[name]
	else:
		print "Oops I guess you have misspelt"

if __name__=="__main__":
	bday_dict = name_look_dictionary()
	user_interaction_birthday_find(bday_dict)
