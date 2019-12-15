import random
import string

def game(guessList, secretList):
    cows = 0
    bulls = 0

    for x in range(0,4):
        if guessList[x] == secretList[x]:
            cows += 1
        else:
            for y in range(0,4):
                if guessList[x] == secretList[y % 4]:
                    bulls += 1

    return str(cows), str(bulls)

if __name__ == "__main__":
    print("Welcome to the Cows and Bulls game! ")
    attempts = 0
    gameState = True
    secretList = random.sample(string.digits, 4)
    print(secretList)
    guess = input("Enter a 4 digit number! (with unique digits) ")

    while(gameState):
        guessList = ([i for i in guess])
        animals = game(guessList, secretList)
        if animals[0] == "4" and animals[1] == "0":
            print(str(animals[0]) + " cow, " + str(animals[1]) + " bull")
            attempts += 1
            print("It took you " + str(attempts) + " attempts!")
            gameState = False
        else:
            print(str(animals[0]) + " cow, " + str(animals[1]) + " bull")
            attempts += 1
            guess = input("Guess again! ")
