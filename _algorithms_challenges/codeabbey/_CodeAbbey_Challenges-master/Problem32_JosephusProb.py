with open("prob32.txt") as infile:
    data = infile.readline()
    n,k = data.split(" ")
    people = [0 for i in range(int(n))] # 0 is alive
    i=0
    while people.count(0) > 1:
        count = 0
        
        while count < int(k)-1 or people[i]!=0:
            if people[i]==0:
                count+=1
            i+=1
            if i >=int(n):
                i=0
##            print(count)
        people[i]=1
##        print(people)
    print(people.index(0)+1)   
            
        
            
        
        
    
