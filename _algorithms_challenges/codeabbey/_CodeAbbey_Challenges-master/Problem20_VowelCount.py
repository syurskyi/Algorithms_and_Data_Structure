with open("prob20.txt") as infile:
    infile.readline()
    data = infile.readlines()

    for line in data:
        count = 0    # resets every line
        for each_char in line:
            if each_char in ["a","e","i","o","u","y"]:
                count+=1

        print(count, end=" ")
        
