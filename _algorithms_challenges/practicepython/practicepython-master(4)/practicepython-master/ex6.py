#to get a input string from a user and print whether its a palindrome or not


user_string = raw_input("Enter  a string to check for palindrome property > ")

new_string = user_string[::-1] #begin:end:increment direction


print "user string is ",user_string

print "reversed string is ",new_string

if user_string == new_string:
	print "The string is a palindrome"

else:
	print "String not a palindrome"



