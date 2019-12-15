def squareroot():
    data = int(input())
    result = ''
    for i in range(data):
        r = 1
        v,steps = map(int, input().split())
        while steps > 0:
            r = (r + v/r) / 2
            steps -= 1
        print(r,'')
    
    
squareroot()