#initializing the number of elements and different types of number 
num_ele, num_type_element = input().split()
num_ele = int(num_ele)
num_ele = int(num_ele)
num_type_element = int(num_type_element)
#print(num_ele, num_type_element)

#to store the elements
ele = []
# unique elements
check = []
#Boolean value to check whether available or no
ava_check = True
#dictionary to store the count of variable
arr_check ={}

while len(ele) < num_ele:
    ele = input().split()
    ele.sort()
    #going through the all the elements
    for i in range(len(ele)):
        #print('starting i',i,'value of ele is',ele[i])
        if len(check)==0:
            check.append(ele[i])
            #checking if the element is with the unique array
        for j in range(0,len(check)):
            #print('starting j',j,' value of ele is',check[j])
            if ele[i] == check[j]:
                ava_check = True
                # if the element is encountered for the first time then store it in dictionary and initialize the count else increment the count
                if ele[i] in arr_check:
                    
                    arr_check[ele[i]] += 1
                    #print('True dictionary',ele[i],'is',arr_check[ele[i]])
                else:
                    
                    arr_check[ele[i]] = 1
                    #print('True else dictionary for ', ele[i],'is',arr_check[ele[i]])
                
            else:
                    ava_check = False
                   
        #if element was not found within the unique list
        #element must be added to the unique list
        #and also must be checked for dictionary
        if ava_check == False:
            #print('value about to be append is:')
            check.append(ele[i])
            if ele[i] in arr_check:

                arr_check[ele[i]] += 1
                #print('False dictionary for',ele[i],'is',arr_check[ele[i]])
            else:

                arr_check[ele[i]] = 1
                #print('False else dictionary for ', ele[i],'is',arr_check[ele[i]])
            #print(check)
            
#finally print the element count
for i,v in arr_check.items():
    print(v,end=(' '))