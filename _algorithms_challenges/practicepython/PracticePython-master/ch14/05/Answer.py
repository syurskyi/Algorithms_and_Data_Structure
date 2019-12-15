with open("./sample1.txt", "r+") as sample1:
    with open("./sample2.txt", "w+") as sample2:
        for line in sample1:
            #print(line, end='')
            sample2.write(line)
