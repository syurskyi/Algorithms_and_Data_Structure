#take the number of strings that are needed to be checked
for i in range(int(input())):
    #accept the string
    string = input()
    #store_str is used to store only the brackets
    store_str = []
    #para list is used to check whether the character in string is equal to elements of para
    para = ['(',')','[',']','<','>','{','}']
    # p Dictionary is used to store the pair of the parenthesis
    p = {'(':')','[':']','<':'>','{':'}'}
    
    #here we remove all alphabets, digits and unwanted special characters
    for j in string:
        #if in para list then only form the list
        if j in para:
            store_str.append(j)

    #First step is to check if there are any pair next to each other if yes then pop those two elements from list
    for j in range(len(store_str)):
        for k in range(0, len(store_str)):
            #try and except are used because if a particular key is not present in dictionary p, it can throw error
            try:
                if p[store_str[k]] == str(store_str[k+1]):
                    store_str.pop(k)
                    store_str.pop(k)
            except:
                pass
        if len(store_str) == 1:
            print('0',end=' ')
            checker = False
            break
        elif len(store_str) == 0:
            print('1',end= ' ')
            checker = False
            break
        else:
            checker = True
            pass
    #Step two is once the element next to each other which were pair are removed.
    #then we are left with nested loops
    #if the starting element and the last element of the list are same then pop, else the give string is not nested properly
    # and the result is 0
    if checker == True:
        while len(store_str) != 1:
            try:
                if p[store_str[0]] == store_str[-1]:
                    store_str.pop(0)
                    store_str.pop(-1)
                else:
                    break
            except:
                break
        if len(store_str) == 0:
            print('1',end=' ')
        elif len(store_str) == 1 or len(store_str) > 1:
            print('0',end=' ')