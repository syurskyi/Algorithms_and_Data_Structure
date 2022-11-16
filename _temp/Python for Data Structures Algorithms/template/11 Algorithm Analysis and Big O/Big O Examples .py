# %%
'''
# Big O Examples
In the first part of the Big-O example section we will go through various iterations of the various Big-O functions.
Make sure to complete the reading assignment!
Let's begin with some simple examples and explore what their Big-O is.

## O(1) Constant
'''

# %%
___ func_constant(values
    '''
    Prints first item in a list of values.
    '''
    print(values[0])
    
func_constant([1,2,3])

# %%
'''
Note how this function is constant because regardless of the list size, the function will only ever take a constant 
step size, in this case 1, printing the first value from a list. so we can see here that an input list of 100 values 
will print just 1 item, a list of 10,000 values will print just 1 item, and a list of **n** values will print just 
1 item!
'''

# %%
'''
## O(n) Linear
'''

# %%
___ func_lin(lst
    '''
    Takes in list and prints out all values
    '''
    ___ val __ lst:
        print(val)
        
func_lin([1,2,3])

# %%
'''
This function runs in O(n) (linear time). This means that the number of operations taking place scales linearly with n, 
so we can see here that an input list of 100 values will print 100 times, a list of 10,000 values will print 
10,000 times, and a list of **n** values will print **n** times.
'''

# %%
'''
## O(n^2) Quadratic
'''

# %%
___ func_quad(lst
    '''
    Prints pairs for every item in list.
    '''
    ___ item_1 __ lst:
        ___ item_2 __ lst:
            print(item_1,item_2)
            
lst _ [0, 1, 2, 3]

func_quad(lst)

# %%
'''
Note how we now have two loops, one nested inside another. This means that for a list of n items, we will have 
to perform n operations for *every item in the list!* This means in total, we will perform n times n assignments, 
or n^2. So a list of 10 items will have 10^2, or 100 operations. You can see how dangerous this can get for very 
large inputs! This is why Big-O is so important to be aware of!
'''

# %%
'''
______
## Calculating Scale of Big-O
In this section we will discuss how insignificant terms drop out of Big-O notation.
When it comes to Big O notation we only care about the most significant terms, remember as the input grows larger 
only the fastest growing terms will matter. If you've taken a calculus class before, this will reminf you of taking 
limits towards infinity. Let's see an example of how to drop constants:
'''

# %%
___ print_once(lst
    '''
    Prints all items once
    '''
    ___ val __ lst:
        print(val)

# %%
print_once(lst)

# %%
'''
The print_once() function is O(n) since it will scale linearly with the input. What about the next example?
'''

# %%
___ print_3(lst
    '''
    Prints all items three times
    '''
    ___ val __ lst:
        print(val)
        
    ___ val __ lst:
        print(val)
        
    ___ val __ lst:
        print(val)

# %%
print_3(lst)

# %%
'''
We can see that the first function will print O(n) items and the second will print O(3n) items. However for n going
 to inifinity the constant can be dropped, since it will not have a large effect, so both functions are O(n).

Let's see a more complex example of this:
'''

# %%
___ comp(lst
    '''
    This function prints the first item O(1)
    Then is prints the first 1/2 of the list O(n/2)
    Then prints a string 10 times O(10)
    '''
    print(lst[0])
    
    midpoint _ len(lst)/2
    
    ___ val __ lst[:midpoint]:
        print(val)
        
    ___ x __ range(10
        print('number')

# %%
lst _ [1,2,3,4,5,6,7,8,9,10]

comp(lst)

# %%
'''
So let's break down the operations here. We can combine each operation to get the total Big-O of the function:
$$O(1 + n/2 + 10)$$
We can see that as n grows larger the 1 and 10 terms become insignificant and the 1/2 term multiplied against n will 
also not have much of an effect as n goes towards infinity. This means the function is simply O(n)!
'''

# %%
'''
## Worst Case vs Best Case
Many times we are only concerned with the worst possible case of an algorithm, but in an interview setting its 
important to keep in mind that worst case and best case scenarios may be completely different Big-O times. 
For example, consider the following function:
'''

# %%
___ matcher(lst,match
    '''
    Given a list lst, return a boolean indicating if match item is in the list
    '''
    ___ item __ lst:
        __ item == match:
            r_ True
    r_ False

# %%
lst

# %%
matcher(lst,1)

# %%
matcher(lst,11)

# %%
'''
Note that in the first scenario, the best case was actually O(1), since the match was found at the first element. 
In the case where there is no match, every element must be checked, this results in a worst case time of O(n). 
Later on we will also discuss average case time.
Finally let's introduce the concept of space complexity.
## Space Complexity
Many times we are also concerned with how much memory/space an algorithm uses. The notation of space complexity 
is the same, but instead of checking the time of operations, we check the size of the allocation of memory.
Let's see a few examples:
'''

# %%
___ printer(n_10
    '''
    Prints "hello world!" n times
    '''
    ___ x __ range(n
        print('Hello World!')

# %%
printer()

# %%
'''
Note how we only assign the 'hello world!' variable once, not every time we print. So the algorithm has O(1) 
**space** complexity and an O(n) **time** complexity. 
Let's see an example of O(n) **space** complexity:
'''

# %%
___ create_list(n
    new_list _ []
    
    ___ num __ range(n
        new_list.append('new')
    
    r_ new_list

# %%
print(create_list(5))

# %%
'''
Note how the size of the new_list object scales with the input **n**, this shows that it is an O(n) algorithm 
with regards to **space** complexity.
_____

Thats it for this lecture, before continuing on, make sure to complete the homework assignment below:
'''

# %%
'''
# Homework Assignment
Your homework assignment after this lecture is to read the fantastic explanations of Big-O at these two sources:
* [Big-O Notation Explained](http://stackoverflow.com/questions/487258/plain-english-explanation-of-big-o/487278#487278)
* [Big-O Examples Explained](http://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly)
'''