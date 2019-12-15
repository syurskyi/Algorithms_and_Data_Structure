import re

def count_words(sentence):
    results = {}
    words = re.findall(r"[a-zA-Z0-9]+'?[a-zA-Z0-9]+|[a-zA-Z0-9]", sentence.lower())
    print(words)
    for word in words:
        if word.lower() not in results:
            results[word.lower()] = words.count(word)
    return results
