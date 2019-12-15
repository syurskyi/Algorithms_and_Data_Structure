# this a called a rock and scissor game
# rules rock beats scissors, scissors beat papers, paper beats rock
import sys


player1 = raw_input(" Enter player 1 name > ")

player2 = raw_input(" Enter player 2 name > ")


while True:
	player1_input = raw_input(" Hi "+player1+" choose any one  rock/scissor/paper> ")
	player2_input = raw_input(" Hi "+player2+" choose any one  rock/scissor/paper> ")
	
	if player1_input == player2_input:
		print "tie"
	elif player1_input == "rock":
		if player2_input == "scissors":
			print player1+" win"
		elif player2_input == "paper":
			print player2+" win"
	elif player1_input == "scissor":
		if player2_input == "rock":
			print player2+" win"
		elif player2_input == "paper":
			print player1+" win"
	elif player1_input == "paper":
		if player2_input == "rock":
			print player1+" win"
		elif player2_input == "scissor":
			print player2+" win"
	else:
		print "Invalid input given"
		sys.exit()

	continue_game = int(raw_input("Do you want to play again ? yes - \
1 no - 0"))

	if continue_game!=1:
		break

print "Bye"

