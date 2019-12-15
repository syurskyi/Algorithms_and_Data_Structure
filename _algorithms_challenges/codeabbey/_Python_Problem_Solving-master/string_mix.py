#accepting the two strings
s1 = ''.join(i for i in input() if i.islower())
s2 = ''.join(i for i in input() if i.islower())
#using sorted to arrange the string in order before processing them
s1 = sorted(s1)
s2 = sorted(s2)

#defining the method mix
def mix(s1,s2):
    
    s1 = ''.join(i for i in s1 if i.islower())
    s2 = ''.join(i for i in s2 if i.islower())

    s1 = sorted(s1)
    s2 = sorted(s2)
    #s1_dic is used to store the count of occurance of a particular
    #alphabet in string s1 and similarly of s2_dic for string s2
    s1_dic = {}
    s2_dic = {}
    
    #sub_str is used to store the alphabets for the number of counts(iterations)
    # for example: count of n is 5 thus sub_str will hold sub_str = 'nnnnn'
    sub_str = ''
    
    #main_string holds the final string that is to be returned
    main_string = ''
    
    #res_string is used to store the sub_str for alphabets and then later it is sorted
    res_string = []

    #this for loop is used to record the count of a particular alphabet in the dictionary for string s1
    for i in s1:
        count = s1.count(i)
        #check if the current character is present in dictionary. if not then add the char to dictionary
        if i not in s1_dic:
            s1_dic[i] = count
    #this for loop is used to record the count of a particular alphabet in the dictionary for string s2
    for i in s2:
        count = s2.count(i)
        #check if the current character is present in dictionary. if not then add the char to dictionary
        if i not in s2_dic:
            s2_dic[i] = count

    #print(s1_dic)
    #print(s2_dic)
    
    # to check the if the same element are present in both the dictionary of s1 and s2
    for i in s1_dic:
        sub_str = ''
        if i in s2_dic:
            #here the count>1 constraint is taken care of 
            if s1_dic[i] > 1 or s2_dic[i] > 1:
                #if the same element is present in both s1 and s2 and count is same
                if s1_dic[i] == s2_dic[i]:
                    for j in range(s1_dic[i]):
                        sub_str += i
                    res_string.append('=:' + sub_str)
                #if the same element is present in both s1 and s2 and count of s1 is greater than s2
                elif s1_dic[i] > s2_dic[i]:
                    for j in range(s1_dic[i]):
                        sub_str += i
                    res_string.append('1:' + sub_str)
                else:
                    for j in range(s2_dic[i]):
                        sub_str += i
                    res_string.append('2:' + sub_str)
        else:
            if s1_dic[i] > 1:
                for j in range(s1_dic[i]):
                    sub_str += i
                res_string.append('1:' + sub_str)
                
    for i in s2_dic:
        sub_str = ''
        if i not in s1_dic:
            if s2_dic[i] > 1:
                for j in range(s2_dic[i]):
                    sub_str += i
                res_string.append('2:' + sub_str)
                
            
                    
        

# Once we got the string here the problem is that it is not sorted the form that is desired
#so the next few cycles will help us to sort the given string according to the desired result
#here the string is sorted on the basis of the length of the string
    
    for i in range(len(res_string)):
        for j in range(0,len(res_string)-1):
            
            # check if the string is less than the next item in the list if yes swap the two string
            if len(res_string[j]) < len(res_string[j+1]):
                res_string[j],res_string[j+1]= res_string[j+1],res_string[j]
            
            #check if the string is having the same lenth
            elif len(res_string[j]) == len(res_string[j+1]):
               
                #check if the string first element is integer or has a '=' 
                #here try and except block helps program from terminating
                try:
                    #convert the strings first element to float 
                    check_int1 = float(res_string[j][0])
                    check_int2 = float(res_string[j+1][0])
                    #if the variable is in integer form then proceed
                    if check_int1.is_integer() and check_int2.is_integer():
                        
                        #Here we check if the integer is greater or no if yes then swap
                        if check_int1 > check_int2:
                            res_string[j],res_string[j+1]=res_string[j+1],res_string[j]
                            
                        #if the integer is equal then we check for the 
                        #precedence of the char in alphabet set and sort accordingly
                        elif check_int1 == check_int2:
                            if res_string[j][2] > res_string[j+1][2]:
                                res_string[j],res_string[j+1]=res_string[j+1],res_string[j]
                except:
                    
                    #if jth and j+1th element has = sign then proceed
                    if res_string[j][0] == '=' and res_string[j+1][0] == '=':
                        
                        #if the char of jth is greater than j+1th char then swap
                        if res_string[j][2] > res_string[j+1][2]:
                            res_string[j],res_string[j+1]=res_string[j+1],res_string[j]
                            
                    # if the jth element is having the '=' sign then it is swaped
                    elif res_string[j][0] == '=':
                        res_string[j],res_string[j+1] = res_string[j+1],res_string[j]
                    
                    else:
                        pass
            else:
                pass
    
    
    main_string = '/'.join(str(e) for e in res_string)
    return main_string
    
mix(s1,s2)