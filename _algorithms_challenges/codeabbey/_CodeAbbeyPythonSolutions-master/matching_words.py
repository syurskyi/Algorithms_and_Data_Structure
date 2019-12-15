results = []
words = input()
words_list = list(words.split())[:-1]
words_list.sort()

word = ""
for i in words_list:
    if(words.index(i) == words.index(word) and i not in results):
        results.append(i)        
    word = i

print(*results)