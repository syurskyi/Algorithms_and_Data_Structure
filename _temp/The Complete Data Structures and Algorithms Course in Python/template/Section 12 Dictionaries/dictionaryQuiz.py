#   Created by Elshad Karimov on 26/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved

# Dictionary Interview Questions


# Q-1. What will be the output of the following code snippet?

a _ {(1,21,(2,32}
print(a[1,2])
# A. Key Error
# B.  1
# C. {(2,3):2}
# D. {(1,2):1}
 

# Q-2. What will be the output of the following code snippet?

a _ {'a':1,'b':2,'c':3}
# print (a['a','b'])
# A. Key Error
# B. [1,2]
# C. {‘a’:1,’b’:2}
# D. (1,2)

 

# Q-3. What will be the output of the following code block?

fruit _ {}

___ addone(index
    __ index __ fruit:
        fruit[index] +_ 1
    ____
        fruit[index] _ 1
        
addone('Apple')
addone('Banana')
addone('apple')
print (len(fruit))
# A. 1 
# B. 2
# C. 3 
# D. 4

 

# Q-4. What will be the output of the following code block?

arr _ {}
arr[1] _ 1
arr['1'] _ 2
arr[1] +_ 1

sum _ 0
___ k __ arr:
    sum +_ arr[k]

print(sum)
# A. 1 
# B. 2
# C. 3 
# D. 4

 

# Q-5. What will be the output of the following code snippet?

my_dict _ {}
my_dict[1] _ 1
my_dict['1'] _ 2
my_dict[1.0] _ 4

sum _ 0
___ k __ my_dict:
    sum +_ my_dict[k]
    
print (sum)
# A. 7
# B. Syntax error
# C. 3
# D. 6

 

# Q-6. What will be the output of the following code snippet?

my_dict _ {}
my_dict[(1,2,4)] _ 8
my_dict[(4,2,1)] _ 10
my_dict[(1,2)] _ 12

sum _ 0
___ k __ my_dict:
    sum +_ my_dict[k]

print (sum)
print(my_dict)
# A. Syntax error
# B. 30   
#     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# C. 47
#     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# D. 30
#     {[1, 2]: 12, [4, 2, 1]: 10, [1, 2, 4]: 8}

 

# Q-7. What will be the output of the following code snippet?

box _ {}
jars _ {}
crates _ {}
box['biscuit'] _ 1
box['cake'] _ 3
jars['jam'] _ 4
crates['box'] _ box
crates['jars'] _ jars
# print(len(crates[box]))
# A. 1
# B. 3
# C. 4
# D. Type Error

 

# Q-8. What will be the output of the following code block?

dict _ {'c': 97, 'a': 96, 'b': 98}

___ _ __ sorted(dict
    print (dict[_])
# A. 96 98 97
# B. 96 97 98
# C. 98 97 96
# D. NameError

 

# Q-9. What will be the output of the following code snippet?

rec _ {"Name" : "Python", "Age":"20"}
r _ rec.copy()
print(id(r) == id(rec))
# A. True
# B. False
# C. 0
# D. 1

 

# Q-10. What will be the output of the following code snippet?

rec _ {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 _ id(rec)
del rec
rec _ {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 _ id(rec)
print(id1 == id2)
# A. True
# B. False
# C. 1
# D. Exception