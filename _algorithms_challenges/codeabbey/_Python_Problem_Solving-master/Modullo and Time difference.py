data = int(input())
string = ''

for i in range(data):
    a = [int(j) for j in input().split()]
    dest_a = a[:len(a)//2]
    dest_b = a[len(a)//2:]
    day_a, hour_a, min_a,sec_a = dest_a
    day_b, hour_b, min_b,sec_b = dest_b
    
    #checking if seconds are greater or no
    if sec_a > sec_b:
        #borrow 1 min i.e 60 secs from mins
        min_b -= 1
        sec = (sec_b + 60) - sec_a
    else:
        sec = sec_b -sec_a
        
    #checking if seconds are greater or no
    if min_a > min_b:
        #borrow 1 hour i.e 60 mins from hour
        hour_b -= 1
        mino = (min_b + 60) - min_a
    else:
        mino = min_b - min_a
        
    #checking if hour are greater or no
    if hour_a > hour_b:
        #borrow 1 day i.e 24 hours from day
        day_b = day_b - 1
        hour = (hour_b + 24) - hour_a
    else:
        hour = hour_b - hour_a
    
    day = day_b - day_a
    
    string += '('+str(int(day))+' '+str(int(hour))+' '+str(int(mino))+' '+str(int(sec))+')'
    string += ' '
    
print(string)