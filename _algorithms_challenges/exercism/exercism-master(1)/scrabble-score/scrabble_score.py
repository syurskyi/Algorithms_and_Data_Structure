def score(word):
    scores = 0
    for character in word:
        for chars, score in {
            "aeioulnrst": 1,
            "dg": 2,
            "bcmp": 3,
            "fhvwy": 4,
            "k": 5,
            "jx": 8,
            "qz": 10
        }.items():
            if character.lower() in chars:
                scores += score
    return scores
