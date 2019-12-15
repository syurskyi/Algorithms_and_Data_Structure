#getting the birthday dates from a json

import json
import ex33
def load_bday_from_json():
	birthday_json = dict()
	with open("birthday_json.json","r") as file_object:
		birthday_json = json.load(file_object)

	return birthday_json

def add_birthday_to_dict_and_json(bday_json,filename):
	print "Enter the name of scientist yo want to add to the dictionary"
	name = raw_input("> ")
	print "Enter the DOB in dd/mm/yyyy format"
	dob = raw_input("> ")
	bday_json[name.strip()] = dob.strip()
	print bday_json
	with open(filename, "w") as f:
    		json.dump(bday_json, f)
	print "new scientist added to birthday list"

if __name__=="__main__":

	birthday_json = load_bday_from_json() 
	ex33.user_interaction_birthday_find(birthday_json)
	add_birthday_to_dict_and_json(birthday_json,"birthday_json.json")

