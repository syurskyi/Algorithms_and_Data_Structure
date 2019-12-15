#tic tac toe user input


def get_coordinate():
	user_input = raw_input("X,Y> ")

	string_input = user_input.strip(' ')
	string_list = string_input.split(',')
	print string_list

	temp =	[xylist for xylist in string_list] 
	xy = [int(temp[0])-1, int(temp[1])-1]
	return xy


#get_coordinate()

def place_icon(matrix,icon,xylist):
	x = xylist[0]
	y = xylist[1]
	if(matrix[x][y] == 0):
		matrix[x][y] = icon
	else:
		print "already taken"
		
	print matrix[0]
	print matrix[1]
	print matrix[2]
	return 0

def play_game(matrix):
	squares = 9;
	
	print matrix[0]
	print matrix[1]
	print matrix[2]
	print "lets start the game player one and two enter x,y coordinates when prompted or q to quit "
	#userinput = "start"
	while squares>0:
		print "player 1 chance "
		
		p1_xy = get_coordinate()
		if matrix[p1_xy[0]][p1_xy[1]] != 0:
			print "already taken enter again"
			continue
		else:
			icon = 'X'
			place_icon(matrix,icon,p1_xy)
			squares -= 1
			#print squares
		if squares == 0:
			break

                print "player 2 chance "

                p2_xy = get_coordinate()
                if matrix[p2_xy[0]][p2_xy[1]] != 0:
                        print "already taken enter again"
                        continue
                else:
                        icon = '@'
                        place_icon(matrix,icon,p2_xy)
			squares-=1
			#print squares
	return matrix # return the matrix for the final module to winner check

if __name__ == "__main__":
        matrix = [ [0,0,0],
                   [0,0,0],
                   [0,0,0]]

	play_game(matrix)
