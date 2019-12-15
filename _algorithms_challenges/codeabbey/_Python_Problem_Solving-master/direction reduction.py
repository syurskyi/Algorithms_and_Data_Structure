#accepting the directions from the user
direction = list(map(str, input().split()))
#Modifying the directions to uppercase
direction = [x.upper() for x in direction]

#defining the definition of the direction reduction
def dirReduc(dir = []):
    #traversing through all the elements of the list
    for j in range(len(dir)):
        #traversing through all the elements except the last one
        for i in range(0,len(dir)-1):
            if dir[i] == 'NORTH' and dir[i+1] == 'SOUTH' or dir[i] == 'SOUTH' and dir[i+1] == 'NORTH':
                dir.pop(i)
                dir.pop(i)  
                break
            elif dir[i] == 'WEST' and dir[i+1] == 'EAST' or dir[i] == 'EAST' and dir[i+1] == 'WEST':
                dir.pop(i)
                dir.pop(i)
                break
            else:
                pass
    #print the result of the direction reduction
    print(dir)
#calling the direction reduciton function
dirReduc(direction)

#north south south east west north west