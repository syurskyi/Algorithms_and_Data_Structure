#accept the input number of people in the circle and counter after which people in the circle will be killed
n,k = map(int,input().split())
#initialize the list in which the number of people will be stored
sucide_squad = []
#store the number of people
for i in range(1,n+1):
    sucide_squad.append(i)
#initialize the counter for killing people in list
counter = 0
# to keep the count of the people and rotate when the list reaches its end
squad_count = 0
#while there is only one element left inside the list
while len(sucide_squad) != 1:
    #increment the counter by 1
    counter += 1
    #check if the counter has reached the final value of killing people. if yes then kill the person who comes at count k
    if counter == k:  
        #when k is reached the pop the person out of the list
        sucide_squad.pop(squad_count)
        #reset the counter to 0
        counter = 0
        #check if the list has reached its limit
        if squad_count == len(sucide_squad):
            #reset the count to 0
            squad_count = 0
        #continue helps not jumping on the next element and start counting from the current element itself
        continue
    squad_count +=1
    #check if reached end of the list
    if squad_count == len(sucide_squad):
        squad_count = 0
print(sucide_squad[0])