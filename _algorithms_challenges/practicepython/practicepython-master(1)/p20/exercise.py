import random

def binarySearch(orderedList, searchTerm, start, end):
    index = int((start + end) / 2)

    if start > end:
        return False
    elif searchTerm == orderedList[index]:
        return True
    elif searchTerm < orderedList[index]:
        return binarySearch(orderedList, searchTerm, start, index-1)
    else:
        return binarySearch(orderedList, searchTerm, index + 1, end)

if __name__ == "__main__":
    orderedList = sorted(int(1000*random.random()) for i in range(1000))
    print(orderedList)
    searchTerm = int(input("Enter a number to search for from 0-999: "))
    print(binarySearch(orderedList, searchTerm, 0, len(orderedList)-1))
