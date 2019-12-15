values = list(map(int, input().split()))

def get_max_and_min():
    max = values[0]
    min = values[0]
    for i in values:
        if(i < min):
            min = i
        elif(i > max):
            max = i
    
    return max, min

max, min = get_max_and_min()

print(max, min)