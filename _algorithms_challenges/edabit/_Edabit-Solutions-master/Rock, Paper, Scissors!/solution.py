def calculate_score(games):
    abigail = 0
    ben = 0
    index = 0
    while index < len(games):
        if games[index][0] == "R" and games[index][1] == "S":
            abigail += 1

        elif games[index][0] == "P" and games[index][1] == "R":
            abigail += 1
        elif games[index][0] == "S" and games[index][1] == "P":
            abigail += 1

        elif games[index][0] == "S" and games[index][1] == "R":
            ben += 1
        elif games[index][0] == "R" and games[index][1] == "P":
            ben += 1
        elif games[index][0] == "P" and games[index][1] == "S":
            ben += 1
        index += 1

    if abigail > ben:
        return "Abigail"
    elif abigail == ben:
        return "Tie"
    else:
         return "Benson"
