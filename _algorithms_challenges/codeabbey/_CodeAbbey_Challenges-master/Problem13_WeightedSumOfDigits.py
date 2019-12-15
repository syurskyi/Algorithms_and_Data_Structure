with open("prob13.txt") as infile:
    infile.readline()
    data=  infile.read()
    data = data.split(" ")
    
    for num in data:
        wsd = 0
        for i in range(len(num)):
            wsd += (i+1)*int(num[i])
        print(wsd, end =" ")
