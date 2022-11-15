# a1 >= a2 <= a3 >= a4 <= a5.....
# [1,2,3,4,5,6] => [2,1,4,3,6,5]
# [1,2] => [2,1] #2
# [1,2,3] => [2,1,3] #3
def make_wave(l):
    for i in range(0,len(l) - 1,2):
        #pair i, i+1
        l[i],l[i+1] = l[i+1],l[i]

l = [1,2,3,4,5,6]
make_wave(l)
print(l)

