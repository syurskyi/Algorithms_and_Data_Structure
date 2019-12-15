x = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

store_add = []
count = 0
for i in x:
    i = list(i)
    j = 0
    plus_check = False
    string = ''
    while i[j]!= '@':
        if plus_check == False:
            if i[j] == '.':
                i.pop(j)
            elif i[j] == '+':
                plus_check = True
            else:
                j += 1
                pass
        else:
            i.pop(j)
    string = ''.join(i)
    if string not in store_add:
        store_add.append(string)
        count += 1
    
return(count)    