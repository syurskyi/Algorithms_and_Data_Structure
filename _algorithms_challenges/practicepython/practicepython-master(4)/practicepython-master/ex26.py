#check tic tac toe for winner alone


#where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

import numpy 
def check_tictac_winner_line(matrix):
#	print matrix[0][0]
	
	for i in range(len(matrix)):
		#print matrix[i]
		row_set = set(matrix[i])
		if len(row_set) == 1 and matrix[i][0]!=0:
			return matrix[i][0]
			
	
	return -1

def check_tictac_winner_diagonal(matrix):
	
	if(matrix[0][0] == matrix[1][1] == matrix[2][2]):
		if matrix[0][0] != 0:
			return matrix[0][0]
	if(matrix[0][2] == matrix[1][1] == matrix[2][0]):
		if matrix[0][2] != 0:
			return matrix[0][2]
	return -1


def check_tic_tac_winner(game):
	winner = check_tictac_winner_line(game)
        #print winner
	if(winner !=-1):
		 return winner
        transpose = numpy.transpose( game)
        winner = check_tictac_winner_line(transpose)
        #print winner
        if(winner !=-1): 
                 return winner
        winner = check_tictac_winner_diagonal(game)
        #print winner
        if(winner !=-1): 
                 return winner


if __name__ == "__main__":
	
	print "winner 1\n"
	game = [[1, 2, 0],
		[2, 1, 0],
		[2, 1, 1]]

	print check_tic_tac_winner(game)
	

	print "winner 2 \n"
	winner_is_2 = [[2, 2, 0],
		[2, 1, 0],
		[2, 1, 1]]
	
	print check_tic_tac_winner(winner_is_2)

	
	print "winner is 1\n"
	winner_is_1 = [[1, 2, 0],
		[2, 1, 0],
		[2, 1, 1]]
	print check_tic_tac_winner(winner_is_1)
	
	print "winner is also 1 \n"
	winner_is_also_1 = [[0, 1, 0],
		[2, 1, 0],
		[2, 1, 1]]
	print check_tic_tac_winner(winner_is_also_1)

	print "no winner for this game\n"
	no_winner = [[1, 2, 0],
		[2, 1, 0],
		[2, 1, 2]]
	print check_tic_tac_winner(no_winner)
	
	print "this game also no winner\n"
	also_no_winner = [[1, 2, 0],
			[2, 1, 0],
			[2, 1, 0]]
	print check_tic_tac_winner(also_no_winner)
