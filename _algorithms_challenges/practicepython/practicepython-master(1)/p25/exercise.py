print("Think of a number between 0 and 99 and I'll try to guess it. ")
print("Enter 'a' if too high, 'b' if too low, 'c' if correct")
count = 1
possibleAnswers = range(0,100)
start = possibleAnswers[0]
end = possibleAnswers[len(possibleAnswers)-1]

while True:
    midpoint = int((start + end + 1)/2)
    print(str(midpoint)+ "?")
    check = input()
    if check == 'c':
        break
    elif check == 'a':
        end = possibleAnswers[midpoint]
        count += 1
    elif check == 'b':
        start = possibleAnswers[midpoint]
        count += 1

print("It took " + str(count) + " tries!")
