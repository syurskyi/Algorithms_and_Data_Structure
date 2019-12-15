#take the input of how many elements you want
data = int(input())
# take the input of the numbers to be sorted
a = [int(num) for num in input().split()]

#create a dictionary to store the index of the list
ele = {}
#create the string to store the position of the sorted index
string = ''

#storing the index of the elements
for x in range(len(a)):
    ele[a[x]] = x+1
    
#sorting the array using the bubble sort
for i in range(len(a)):
    for j in range(0,len(a)-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        else:
            pass
#identifying the elements which are sorted with the dictionary key and printing the original index in sorted form
for ele_list in a:
    for dic in ele.keys():
        if ele_list == dic:
            string +=str(ele[dic])
            string +=' '
            
print(string)