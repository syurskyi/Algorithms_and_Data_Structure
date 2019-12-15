with open("prob41.txt") as infile:
    infile.readline()
    data = infile.readlines()
    
    for line in data:
        numbers = line.strip().split(" ")
        numbers = [int(i) for i in numbers]
        numbers = sorted(numbers)  
        print(numbers[1],end=" ")
        
        
