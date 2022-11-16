# Sequential Search
# Check out the video lecture for a full breakdown, in this Notebook all we do is implement Sequential Search for
# an Unordered List and an Ordered List.
# Sequential Search

___ seq_search(arr,ele
    """
    General Sequential Search. Works on Unordered lists.
    """

    # Start at position 0
    pos _ 0
    # Target becomes true if ele is in the list
    found _ False

    # go until end of list
    _____ pos < len(arr) and n.. found:

        # If match
        __ arr[pos] == ele:
            found _ True

        # Else move one down
        ____
            pos  _ pos+1

    r_ found

arr _ [1,9,2,8,3,4,7,5,6]

print seq_search(arr,1)
# True
#
print seq_search(arr,10)
# False
#
# Ordered List
#
# If we know the list is ordered than, we only have to check until we have found the element or an element greater
# than it.

___ ordered_seq_search(arr,ele
    """
    Sequential search for an Ordered list
    """
    # Start at position 0
    pos _ 0

    # Target becomes true if ele is in the list
    found _ False

    # Stop marker
    stopped _ False

    # go until end of list
    _____ pos < len(arr) and n.. found and n.. stopped:

        # If match
        __ arr[pos] == ele:
            found _ True

        ____

            # Check if element is greater
            __ arr[pos] > ele:
                stopped _ True

            # Otherwise move on
            ____
                pos  _ pos+1

    r_ found

arr.sort()

ordered_seq_search(arr,3)
# True
#
ordered_seq_search(arr,1.5)
# False
#
# Good Job!