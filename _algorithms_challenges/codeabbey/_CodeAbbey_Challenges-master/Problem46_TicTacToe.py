infile = open("prob46.txt")
infile.readline()
data = infile.readlines()
infile.close()

win = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]

for line in data:
    moves = line.strip().split(" ")
    x= [int(i) for i in moves if moves.index(i)%2==0]
    o= [int(i) for i in moves if moves.index(i)%2==1]
    highest_x = 0
    highest_o = 0
    for i in range(len(moves)):
        if i%2 == 0 :
            for j in win:
                temp_x = [i for i in x if i in j]
                if len(temp_x) == 3:
                    highest_x = max([moves.index(str(i)) for i in temp_x])
                    break
        else:
            for j in win:
                temp_o = [i for i in o if i in j]
                if len(temp_o) == 3:
                    highest_o = max([moves.index(str(i)) for i in temp_o])
                    break
                
    if highest_x == 0 and highest_o == 0:
        print("0",end=" ")
    elif highest_x ==0 or highest_o ==0:
        print(highest_x+1 if highest_o==0 else highest_o+1,end= " ")
    elif highest_x < highest_o:
        print(highest_x+1,end=" ")
    else:
        print(highest_o+1,end=" ")
            
            
    
    
        
