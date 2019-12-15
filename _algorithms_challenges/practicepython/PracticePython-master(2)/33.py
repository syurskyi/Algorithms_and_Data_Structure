# Birthday Dictionary

# Welcome Message
print ("Welcome to the birthday dictionary. We know the birthdays of:")
name_dictionary = {
    "Einstein": "01/01/2018",
    "Franklin": "01/17/1706",
    "Lovelace": "01/01/2011"
}

# Ask __name__
input = input("Who's birthday do you want to look up?")
if input in name_dictionary:
    print (name_dictionary[input])
else:
    print ("We don't have this person's birthday")
