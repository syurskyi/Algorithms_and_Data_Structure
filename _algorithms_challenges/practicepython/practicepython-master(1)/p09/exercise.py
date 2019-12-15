import random

random.seed()
number = random.randint(1,9)

counter = 0

while True:
    guess = input("guess the number between 1 and 9 inclusive: ")

    if guess == "exit":
        break
    elif int(guess) == number:
        print("correct!")
        break
    elif int(guess) > number:
        print("too high, guess lower!")
        counter += 1
    else:
        print("too low, guess higher!")
        counter += 1

print("it took you " + str(counter) + " guesses!")
