import numpy as np
f = open('input.txt')
res = []

T = int(f.readline().strip())

boards = []
for i in range(0,T):
    boards.append(f.readline().strip().split(' '))

for i in range(T):
    a = [int(j) for j in boards[i]]
    A = np.array([[a[0],1],[a[2],1]])
  
    b = np.array([a[1],a[3]])
    z = np.linalg.solve(A,b)
    if not z[1].is_integer():
        z[1] = z[1] + 0.5
    if z[1] - int(z[1]) < 0:
        z[1] = round(z[1] - 0.5)
        
    if not z[0].is_integer():
        z[0] = z[0] + 0.5
    if z[0] - int(z[0]) < 0:
        z[0] = round(z[0]  - 0.5)
    string = '('+str(int(z[0]))+' '+str(int(z[1]))+')'
    res.append(string)                           
                                  
final = ' '.join(str(e) for e in res)
print(final)