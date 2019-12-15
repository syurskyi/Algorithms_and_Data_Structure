def route_diff(directions):
    output = []
    for i in directions:
        if i == "N":
            if output.count("S") > 0:
                output.remove("S")
            else:
                output.append(i)
        elif i == "E":
            if output.count("W") > 0:
                output.remove("W")
            else:
                output.append(i)
        elif i == "S":
            if output.count("N") > 0:
                output.remove("N")
            else:
                output.append(i)
        elif i == "W":
            if output.count("E") > 0:
                output.remove("E")
            else:
                output.append(i)

    return len(directions) - len(output)
