# Implementation of a Hash Table
# In this lecture we will be implementing our own Hash Table to complete our understanding of Hash Tables and
# Hash Functions! Make sure to review the video lecture before this to fully understand this implementation!
# Keep in mind that Python already has a built-in dictionary object that serves as a Hash Table, you would never
# actually need to implement your own hash table in Python.
# Map
# The idea of a dictionary used as a hash table to get and retrieve items using keys is often referred to as a mapping.
# In our implementation we will have the following methods:
#
#     HashTable() Create a new, empty map. It returns an empty map collection.
#     put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value
#     with the new value.
#     get(key) Given a key, return the value stored in the map or None otherwise.
#     del Delete the key-value pair from the map using a statement of the form del map[key].
#     len() Return the number of key-value pairs stored
#     in the map in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.

c_ HashTable o..

    ___ - size

        # Set up size and slots and data
        size _ size
        slots _ [N..] * size
        data _ [N..] * size

    ___ putkey,data
        #Note, we'll only use integer keys for ease of use with the Hash Function

        # Get the hash value
        hashvalue _ hashfunction(key,l..(slots))

        # If Slot is Empty
        __ slots[hashvalue] __ N..
            slots[hashvalue] _ key
            data[hashvalue] _ data

        ____

            # If key already exists, replace old value
            __ slots[hashvalue] __ key:
                data[hashvalue] _ data

            # Otherwise, find the next available slot
            ____

                nextslot _ rehash(hashvalue,l..(slots))

                # Get to the next slot
                _____ slots[nextslot] !_ N.. ___ slots[nextslot] !_ key:
                    nextslot _ rehash(nextslot,l..(slots))

                # Set new key, if NONE
                __ slots[nextslot] __ N..
                    slots[nextslot]_key
                    data[nextslot]_data

                # Otherwise replace old value
                ____
                    data[nextslot] _ data

    ___ hashfunctionkey,size
        # Remainder Method
        r_ key%size

    ___ rehasholdhash,size
        # For finding next possible positions
        r_ (oldhash+1)%size


    ___ getkey

        # Getting items given a key

        # Set up variables for our search
        startslot _ hashfunction(key,l..(slots))
        data _ N..
        stop _ F..
        found _ F..
        position _ startslot

        # Until we discern that its not empty or found (and haven't stopped yet)
        _____ slots[position] !_ N.. ___ n.. found ___ n.. stop:

            __ slots[position] __ key:
                found _ T..
                ? _ ?[position]

            ____
                position_self.rehash(position,l..(slots))
                __ position __ startslot:

                    stop _ T..
        r_ data

    # Special Methods for use with Python indexing
    ___ __getitem__key
        r_ get(key)

    ___ __setitem__key,data
        put(key,data)

# Let's see it in action!
#
h _ HashTable(5)

# # Put our first key in
h[1] _ 'one'

h[2] _ 'two'

h[3] _ 'three'

h[1]

'one'

h[1] _ 'new_one'

h[1]

'new_one'

print h[4]

# None
#
# Great Job!
# That's it for this rudimentary implementation, try implementing a different hash function for practice!