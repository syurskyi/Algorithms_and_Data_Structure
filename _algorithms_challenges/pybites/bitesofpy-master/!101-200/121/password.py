import re


def password_complexity(password: str):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    up = lo = num = spec = 0
    for l in password:
        if l.isupper():
            up += 1
        elif l.islower():
            lo += 1
        elif l.isdigit():
            num += 1
        else:
            spec += 1
    score = 0
    if 0 < up and 0 < lo:
        score += 1
    if 0 < up + lo and 0 < num:
        score += 1
    if 0 < spec:
        score += 1
    if len(password) >= 8:
        score += 1
        if not re.search(r'(.)\1', password):
            score += 1
    return score
