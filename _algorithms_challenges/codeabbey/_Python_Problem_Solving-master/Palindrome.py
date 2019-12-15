#The word or whole phrase which has the same sequence of letters in both directions is called a palindrome.
for i in range(int(input())):
    rev_str = ''
    string = ''.join(e for e in input().lower() if e.islower())
    #here iam storing the string in the reverse form
    for j in range(len(string)-1,-1,-1):
        rev_str += string[j]
    #once the reverse string is stored then i'm comparing it with the original string
    if rev_str == string:
        print('Y',' ')
    else:
        print('N',' ')