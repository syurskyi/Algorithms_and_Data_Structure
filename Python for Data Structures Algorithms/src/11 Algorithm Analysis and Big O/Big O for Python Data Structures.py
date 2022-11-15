import timeit

# %%
'''
# Big O for Python Data Structures
In this lecture we will go over the Big O of built-in data structures in Python: Lists and Dictionaries.
'''

# %%
'''
# Lists
In Python lists act as dynamic arrays and support a number of common operations through methods called on them. The 
two most common operations performed on a list are indexing and assigning to an index position. These operations are 
both designed to be run in constant time, O(1).
Let's imagine you wanted to test different methods to construct a list that is [0,1,2...10000]. Let go ahead and 
compare various methods, such as appending to the end of a list, concatenating a list, or using tools such as casting 
and list comprehension.

For example:
'''

# %%
def method1():
    l = []
    for n in range(10000):
        l = l + [n]

def method2():
    l = []
    for n in range(10000):
        l.append(n)

def method3():
    l = [n for n in range(10000)]

def method4():
    l = range(10000) # Python 3: list(range(10000))

# %%
'''
Let's now test these methods using the timeit magic function:
'''

# %%
# print(timeit.timeit(method1))
# %timeit method2()
# %timeit method3()
# %timeit method4()

# %%
'''
We can clearly see that the most effective method is the built-in range() function in Python!
It is important to keep these factors in mind when writing efficient code. More importantly begin thinking about how 
we are able to index with O(1). We will discuss this in more detail when we cover arrays general. For now, take 
a look at the table below for an overview of Big-O efficiencies.
'''

# %%
'''
### Table of Big-O for common list operations
** Please note, in order to see this table, you may need to download this .ipynb file and view it locally, 
sometimes GitHub or nbveiwer have trouble showing the HTML for it... **
'''

# %%
'''
<table>
    
        <tr>
            <th>Operation </th>
            <th>Big-O Efficiency</th>
        </tr>
    

    <tr>
        <td>index []</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>index assignment</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>append</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>pop()</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>pop(i)</td>
        <td>O(n)</td>
    </tr>
    <tr >
        <td>insert(i,item)</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>del operator</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>iteration</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>contains (in)</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>get slice [x:y]</td>
        <td>O(k)</td>
    </tr>
    <tr>
        <td>del slice</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>set slice</td>
        <td>O(n+k)</td>
    </tr>
    <tr>
        <td>reverse</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>concatenate</td>
        <td>O(k)</td>
    </tr>
    <tr>
        <td>sort</td>
        <td>O(n log n)</td>
    </tr>
    <tr>
        <td>multiply</td>
        <td>O(nk)</td>
    </tr>

</table>
'''

# %%
'''
# Dictionaries

Dictionaries in Python are an implementation of a hash table. They operate with keys and values, for example:
'''

# %%
d = {'k1':1,'k2':2}

# %%
d['k1']

# %%
'''
Something that is pretty amazing is that getting and setting items in a dictionary are O(1)! Hash tables are designed 
with efficiency in mind, and we will explore them in much more detail later on in the course as one of the most 
important data structures to undestand. In the meantime, refer to the table below for Big-O efficiencies of 
common dictionary operations:

<table border="1">
<thead valign="bottom">
<tr class="row-odd"><th class="head">Operation</th>
<th class="head">Big-O Efficiency</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>copy</td>
<td>O(n)</td>
</tr>
<tr class="row-odd"><td>get item</td>
<td>O(1)</td>
</tr>
<tr class="row-even"><td>set item</td>
<td>O(1)</td>
</tr>
<tr class="row-odd"><td>delete item</td>
<td>O(1)</td>
</tr>
<tr class="row-even"><td>contains (in)</td>
<td>O(1)</td>
</tr>
<tr class="row-odd"><td>iteration</td>
<td>O(n)</td>
</tr>
</tbody>
</table>
'''

# %%
'''
# Conclusion
By the end of this section you should have an understanding of how Big-O is used in Algorithm analysis and be able 
to work out the Big-O of an algorithm you've developed. Get ready, there's a quiz up next!
'''