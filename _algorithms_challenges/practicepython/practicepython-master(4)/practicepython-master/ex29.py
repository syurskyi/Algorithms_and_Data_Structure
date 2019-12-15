#tic tac toe final

import ex26
import ex27

if __name__=="__main__":
        game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
	finalmatrix= ex27.play_game(game)
        print ex26.check_tic_tac_winner(finalmatrix)


	

