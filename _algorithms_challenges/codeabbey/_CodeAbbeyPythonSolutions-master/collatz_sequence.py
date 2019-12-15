amount_values = int(input())
results = []

def get_seq(Xnext, counter=0):
    if(Xnext == 1):
        return counter
    else:
        if(Xnext % 2 == 0):
            return get_seq(Xnext/2, counter+1)
        else:
            return get_seq(3*Xnext+1, counter+1)

XList = list(map(int, input().split()))
for i in XList:
    seq = get_seq(i)
    results.append(seq)

print(*results)