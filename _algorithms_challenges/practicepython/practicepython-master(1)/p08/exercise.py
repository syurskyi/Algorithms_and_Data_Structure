while True:
    player1 = input("player1: rock, paper, or scissors? ")
    player2 = input("player2: rock, paper, or scissors? ")

    if player1 == player2:
        print("it's a tie! prepare for another round.")
        continue
    elif player1 == "rock":
        if player2 == "paper":
            print("player1 wins!")
            break
        else:
            print("player2 wins!")
            break
    elif player1 == "paper":
        if player2 == "rock":
            print("player1 wins!")
            break
        else:
            print("player2 wins!")
            break
    elif player1 == "scissors":
        if player2 == "paper":
            print("player1 wins!")
            break
        else:
            print("player2 wins!")
            break
    else:
        print("invalid input. choose rock, paper, or scissors. please try again.")
