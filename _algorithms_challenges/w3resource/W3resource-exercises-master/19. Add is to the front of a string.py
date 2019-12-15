def addins(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str
print(addins(" kasper here?"))
print(addins("Is anybody hungry?"))