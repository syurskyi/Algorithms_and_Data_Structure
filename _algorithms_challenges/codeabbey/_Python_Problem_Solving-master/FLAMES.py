#accept both names of the couple
name1,name2=a,b = input('Enter the name of a couple of whom you wanna see FUTURE').split()

#remove the similar element from both the string
for i in a:
    if i in b:
        a = a.replace(i,'')
        b = b.replace(i,'')

#take the length of the both the strings after removal of the similar characters
length = len(a) + len(b)

#define a dictionary to simply print the result of the FLAMES
flame_dic = {'F':'Friends','L':'Lover','A':'Affectionate','M':'Marriage','E':'Enemies','S':'Sex'}
#define a list to process the flames 
flame = ['F','L','A','M','E','S']

#count to iterate through the flames list
i = 0
#count of the length of combined strings
len_count = 1
#while there remains only one element in the flames list
while len(flame)!= 1:
    #if length of the combined string has reached then pop the current element of the flames list
    if len_count == length:
        flame.pop(i)
        len_count = 1
        #check if after poping the element has the flames reached the end of the list if yes then reset the i counter
        if i == len(flame):
            i = 0
    else:
        len_count += 1
        i += 1
        #check if the i counter has reached end of the list if yes then reset the counter
        if i >= len(flame):
            i = 0
print('The relationship future of',name1,'&',name2,' is',flame_dic[flame[0]])
    
    