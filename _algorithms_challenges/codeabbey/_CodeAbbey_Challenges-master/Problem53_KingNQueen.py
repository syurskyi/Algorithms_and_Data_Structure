infile = open("prob53.txt")
infile.readline()
data = infile.readlines()
infile.close()

board = [["-" for i in range(8)]for j in range(8)]
col = ["a","b","c","d","e","f","g","h"]

def display():
    global board
    for i in range(8+1):
        if i == 8:
            print("  a b c d e f g h")
            break
        print("{}".format(8-i),end=" ")
        for j in range(8):
            print(board[i][j],end=" ")
        print()


for line in data:
    ########### ALTERNATIVE ######
##    pieces = line.strip()
##    if pieces[0]==pieces[3] or pieces[1]==pieces[4] or abs(int(pieces[0], 20)-int(pieces[3], 20))==abs(int(pieces[1], 20)-int(pieces[4], 20)):
##        print("Y", end=" ")
##    else:
##        print("N", end=" ")
    ####################
    
##    king,queen = line.strip().split(" ")
##    #check ROW & COLUMN
##    if king[0] == queen[0] or king[1] == queen[1]:
##        print("Y",end=" ")
##        continue
##    #check DIAGONAL
##    q = [8-int(queen[1]),col.index(queen[0])]
##    #upper diag
##    queen_moves = []
##    temp_row = q[0]
##    temp_col = q[1]
##    i = 1
##    while temp_row-1 >= 0 and temp_row-1 <8:
##        temp_row -=1
##        if temp_col-i >=0 and temp_col-i <8:
##            queen_moves.append(str(temp_row)+str(temp_col-i))
##        if temp_col+i >=0 and temp_col+i <8:
##            queen_moves.append(str(temp_row)+str(temp_col+i))
##        i+=1
##    temp_row = q[0]
##    temp_col = q[1]
##    i = 1
##    #lower diag
##    while temp_row+1 >= 0 and temp_row+1 <8:
##        temp_row +=1
##        if temp_col-i >=0 and temp_col-i <8:
##            queen_moves.append(str(temp_row)+str(temp_col-i))
##        if temp_col+i >=0 and temp_col+i <8:
##            queen_moves.append(str(temp_row)+str(temp_col+i))
##        i+=1   
##
##    #convert king to coordinate
##    k = [8-int(king[1]),col.index(king[0])]
##    k = "".join([str(i) for i in k])
##    if k in queen_moves:
##        print("Y",end=" ")
##        continue
##    print("N",end=" ")
##    
##        

















        
    
