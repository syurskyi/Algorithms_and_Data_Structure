userinput = str(input("enter a string: "))

reverse = userinput[::-1]

if userinput == reverse:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")
