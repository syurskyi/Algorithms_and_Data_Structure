#password generator program to generate password for an user
import random
import string
def generate_password(length):
	print "generating you password please wait"
	password = ""
	#random.choice('abcdefghijklmnopqrstuvwxyz')
	#random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	#random.choice('1234567890')
	#random.choice('@!#$%^&*-+=/')
	for x in range(0,pwdlen):
		password_code = random.randint(0,3)
		if password_code ==1:
			password += random.choice('abcdefghijklmnopqrstuvwxyz')
		elif password_code == 2:
			password += random.choice('abcdefghijklmnopqrstuvwxyz')
		elif password_code == 3:
			password += random.choice('1234567890')
		else:
			password += random.choice('@!#$%^&*-+=/')

	
	return password



if __name__ == "__main__":
	pwdlen = int(raw_input("Input the length of password you need > "))
	password = generate_password(pwdlen)
	print "Your password is "
	print password
	
	#below string attributes can be used
	#print string.ascii_letters
	#print string.digits
	#print string.punctuation
	print "".join(random.sample(string.ascii_letters+string.digits+string.punctuation , pwdlen))
