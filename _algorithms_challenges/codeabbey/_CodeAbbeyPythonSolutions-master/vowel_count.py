amount_values = int(input())
results = []

def count_vowels(word):
    letters = ["a","o","u","i","e","y"]
    counter = 0
    for i in word:
        if (i in letters):
            counter += 1
    results.append(counter)

for i in range(amount_values):
    word = input()
    count_vowels(word)
    
print(*results)

