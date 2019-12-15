# Element Search - Function
# Lesson: Two variables: def elementsearch (a,ask) and print (elementsearch (a, ask))


def elementsearch(a, ask):
    for i in a:
        if i == ask:
            return True
        else:
            return False


ask = int(input("Give me a number to search: "))
a = [2, 3, 5, 6, 7, 8, 12, 64, 98]

print (elementsearch(a, ask))
