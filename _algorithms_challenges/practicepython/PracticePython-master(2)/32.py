# Hangman - 32

# Part One - Random word
import random

# Retrieve sowpods
with open("sowpods.txt", "r") as f:
    words = []
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)
        # Explain: while loop -- while its on a line
        # read the line, and append it to the list
    # strip removes the \n line break

# Generate random

random_index = random.randint(0, len(words))

# Print the word

print (words[random_index])
