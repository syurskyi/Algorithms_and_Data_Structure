#   Created by Elshad Karimov on 23/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Q-1. What will be the output of the following code block?
a_[1,2,3,4,5,6,7,8,9]
print(a[::2])

# Q-2. What will be the output of the following code snippet?

a_[1,2,3,4,5,6,7,8,9]
a[::2]_10,20,30,40,50,60
print(a)
# A. ValueError: attempt to assign sequence of size 6 to extended slice of size 5
# B. [10, 2, 20, 4, 30, 6, 40, 8, 50, 60]
# C. [1, 2, 10, 20, 30, 40, 50, 60]
# D. [1, 10, 3, 20, 5, 30, 7, 40, 9, 50, 60]


 
# Q-3. What will be the output of the following code snippet?

a_[1,2,3,4,5]
print(a[3:0:-1])
# A. Syntax error
# B. [4, 3, 2]
# C. [4, 3]
# D. [4, 3, 2, 1]


 

# Q-4. What will be the output of the following code snippet?

___ f(value, values
    v _ 1
    values[0] _ 44
t _ 3
v _ [1, 2, 3]
f(t, v)
print(t, v[0])
# A. 1 44
# B. 3 1
# C. 3 44
# D. 1 1


 

# Q-5. What is the correct command to shuffle the following list?

fruit_['apple', 'banana', 'papaya', 'cherry']
# A. fruit.shuffle()
# B. shuffle(fruit)
# C. random.shuffle(fruit)
# D. random.shuffleList(fruit)


 


 
# Q-6. What will be the output of the following code snippet?

data _ [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
___ fun(m
    v _ m[0][0]

    ___ row __ m:
        ___ element __ row:
            __ v < element: v _ element

    r_ v
print(fun(data[0]))
# A. 1
# B. 2
# C. 3 
# D. 4
# E. 5
# F. 6


 

# Q-7. What will be the output of the following code snippet?

arr _ [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
___ i __ range(0, 4
    print(arr[i].pop())
# A. 1 2 3 4
# B. 1 4 8 12
# C. 4 7 11 15 
# D. 12,13,14,15


 

# Q-8. What will be the output of the following code snippet?

___ f(i, values _ []
    values.append(i)
    print (values)
    r_ values
f(1)
f(2)
f(3)
# A. [1] [2] [3]
# B. [1, 2, 3]
# C. [1] [1, 2] [1, 2, 3]
# D. 1 2 3


 

# Q-9. What will be the output of the following code snippet?

arr _ [1, 2, 3, 4, 5, 6]
___ i __ range(1, 6
    arr[i - 1] _ arr[i]
___ i __ range(0, 6
    print(arr[i], end _ " ")
# A. 1 2 3 4 5 6
# B. 2 3 4 5 6 1
# C. 1 1 2 3 4 5 
# D. 2 3 4 5 6 6


 

# Q-10. What will be the output of the following code snippet?

fruit_list1 _ ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 _ fruit_list1
fruit_list3 _ fruit_list1[:]

fruit_list2[0] _ 'Guava'
fruit_list3[1] _ 'Kiwi'

sum _ 0
___ ls __ (fruit_list1, fruit_list2, fruit_list3
    __ ls[0] == 'Guava':
        sum +_ 1
    __ ls[1] == 'Kiwi':
        sum +_ 20

print(sum)
# A. 22
# B. 21
# C. 0
# D. 43

