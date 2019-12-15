s ='HEELLLLOO'
string = ''
for i in range(len(s)):
    if 'A='<= s[i] <= 'Z':
        string += chr((ord(s[i])) + 32)
    else:
        string += s[i]
print(string)