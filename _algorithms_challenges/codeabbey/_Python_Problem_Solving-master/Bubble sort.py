number_elements = int(input())
a = [int(ele) for ele in input().split()]

swap_count = 0
pass_count = 0

# Here we have to compare each adjacent pair
# first loop is to traverse all elements N-1 times and it acts like pass_count
# boolean is required to check whether the array is sorted or no
for i in range(0, len(a)-1):
    swap = False
    #second loop traverse through all elements checking for greater number and sorting them accordingly
    for j in range(len(a)-1):
        #print('\n',i,'comparing ',a[j],'with jth term', a[j+1])
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swap_count += 1
            #print('swaping',swap_count)
            swap= True
            #print(a)
    if swap == False:
        #print('im breaking up')
        break
            
#print(a)
print(i+1,swap_count)
        