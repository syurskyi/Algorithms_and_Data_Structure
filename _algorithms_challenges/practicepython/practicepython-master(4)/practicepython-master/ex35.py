#use to counter data structure collection and how many birthdays come in each month


import ex34

from collections import Counter


def count_birthday_months():
	bday_json = ex34.load_bday_from_json()
	#print bday_json
	#c = Counter(bday_json)
	#print c
	monthlist = []
	for k,v in bday_json.items():
		text = v[3]+v[4]
		monthlist.append(text)
		#print text
	return monthlist


if __name__=="__main__":
	monthlist = count_birthday_months()
	c = Counter(monthlist)
	print c
	for k,v in c.items():
		print "%s : %s"%(k,v)
