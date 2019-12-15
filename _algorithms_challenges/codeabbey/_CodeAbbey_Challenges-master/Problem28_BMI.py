with open("prob28.txt") as infile:
    infile.readline()
    data= infile.readlines()
    for line in data:
        weight,height = line.strip().split(" ")
        bmi = lambda x,y : int(x)/(float(y)**2)
        
        ans =float(bmi(weight,height))
        if ans < 18.5:
            print("under",end=" ")
        elif ans < 25.0:
            print("normal",end=" ")
        elif ans < 30.0:
            print("over",end= " ")
        else:
            print("obese",end=" ")
            
