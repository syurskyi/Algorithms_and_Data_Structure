# ask for number of iterations
num_iter = int(input('Enter the number of iterations:'))
#initialize the starting element of the sequence
start_num = input('Enter the starting string of the sequence:')

#define the function of lookand say
def look_and_say(data,maxlen):
    result = []
    #first iteration to iterate through given iterations by the user
    for i in range(maxlen-1):
        # defining the number of count of a particular character in the string
        count = 1
        #list to store the count of the character and the character
        res_string = []
        #Loop for traversing through the length of the given string
        for k in range(0,len(data)):
            try:
                #check if the next element is same as the previous element and update the count
                if data[k] == data[k+1]:
                    count += 1
                else:
                    #if the next element is different then store the count as well as the character
                    res_string.append(str(count) + data[k])
                    #reinitialize the count
                    count = 1
            except:
                #if the loop has reached its last element then store the count of the character of last element.
                if k == len(data)-1:
                    res_string.append(str(count) + data[k])
        #print the updated string with updated count
        data = ''.join(str(e) for e in res_string)
        result.append(data)
        #print(start_num)
    return result

look_and_say(start_num,num_iter)