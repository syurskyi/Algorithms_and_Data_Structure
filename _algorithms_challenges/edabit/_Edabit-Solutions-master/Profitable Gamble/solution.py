def profitable_gamble(prob, prize, pay):
    if (prob * prize) > pay:
        return True
    else:
        return False
