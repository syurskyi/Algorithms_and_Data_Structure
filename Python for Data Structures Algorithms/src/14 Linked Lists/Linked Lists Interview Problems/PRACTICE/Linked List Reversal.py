# Linked List Reversal
# Problem
# Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return
# the new head of the list.
#
# You are given the example Linked List Node class:
#
class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

# Solution
#
# Fill out your solution below:
#
def reverse(head):
    cur = head
    pre, nxt = None, None
    while cur:# watch out
        nxt = cur.nextnode
        cur.nextnode = pre
        pre = cur
        cur = nxt
    return pre #watch out
    pass

# Test Your Solution
# Note, this isn't a classic run cell for testing your solution, please read the statements below carefully
# You should be able to easily test your own solution to make sure it works. Given the short list a,b,c,d with values
# 1,2,3,4. Check the effect of your reverse function and make sure the results match the logic here below:
#
# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

# Now let's check the values of the nodes coming after a, b and c:

print (a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)

# 2
# 3
# 4

d.nextnode.value
#
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-46-9ee2d814a788> in <module>()
# ----> 1 d.nextnode.value
#
# AttributeError: 'NoneType' object has no attribute 'value'
#
# So far so good. Note how there is no value proceeding the last node, this makes sense! Now let's reverse
# the linked list, we should see the opposite order of values!
#
reverse(a)
# <__main__.Node at 0x1067a2f28>
#
print (d.nextnode.value)
print (c.nextnode.value)
print (b.nextnode.value)
#
# 3
# 2
# 1
#
print a.nextnode.value # This will give an error since it now points to None
#
#   File "<ipython-input-49-42251ca948f9>", line 1
#     print a.nextnode.value # This will give an error since it now points to None
#           ^
# SyntaxError: Missing parentheses in call to 'print'
#
# Great, now we can see that each of the values points to its previous value (although now that
# the linked list is reversed we can see the ordering has also reversed)