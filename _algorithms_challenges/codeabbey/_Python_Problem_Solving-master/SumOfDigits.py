d = int(input())

lista = []
while len(lista) < d:
    result = 0
    num =  input().split()
    mul = int(num[0]) * int(num[1])
    addi = mul + int(num[2]) 

    res = str(addi)    
    
    for i in range(0,len(res)):
        result = result + int(res[i])
    
    lista.append(result)

    
resv =  ' '.join(str(e) for e in lista)
print(resv) 