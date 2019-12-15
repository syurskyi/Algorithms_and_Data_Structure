
#create a 4 digit guessing game where correct guess at correct place gives cow and wrong place 
#gives bull

import random
import sys
def generate_random_4_digits():
	randomlist = random.sample(range(0,10),4)
	return randomlist

def playgame(randomlist):
	#print randomlist
	print "Enter 4 digits"
	a = int(raw_input("digit 1> "))
	b = int(raw_input("digit 2> "))
	c = int(raw_input("digit 3> "))
	d = int(raw_input("digit 4> "))
	print "%d %d %d %d" % (a,b,c,d)
	userlist = []
	userlist.append(a)
	userlist.append(b)
	userlist.append(c)
	userlist.append(d)
	cows = 0
	bulls = 0
	for i in range(0,len(randomlist)):
		if userlist[i] == randomlist[i]:
			cows+=1
		elif userlist[i] in randomlist:
			bulls+=1
	print "%d cows %d bulls"%(cows,bulls)	
	#print randomlist
	if(cows == 4):
		print "4 cows. you guessed it right"
		sys.exit()
	play_input = raw_input("Wanna try again (y/n)> ")
	
	if(play_input=="y"):
		playgame(randomlist)


if __name__ == "__main__":
	randomlist = generate_random_4_digits()
	playgame(randomlist)
