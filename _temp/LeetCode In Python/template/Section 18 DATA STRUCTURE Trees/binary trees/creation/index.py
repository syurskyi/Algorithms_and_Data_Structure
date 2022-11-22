
c_ Node
    ___ -  value
        left _ N..
        right _ N..
        data _ value


# create root
root _ Node(4)

#	    4
#	  /   \
#	None  None


root.left _ Node(5)
root.right _ Node(6)

# 5 becomes left child and 6 become right child of 1
#		           4
#		       /       \
#		      5	        6
#	      /  \      /   \
#     None None  None  None


root.left.left _ Node(7)


# 7 becomes left child of 5
#		           4
#		       /       \
#		      5	        6
#	      /  \      /   \
#      7   None  None  None
#     / \
#  None  None
