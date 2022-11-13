class HashTable:
    ## WRITE HT CONSTRUCTOR HERE ##
    #                             #
    #                             #
    ###############################
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

        
my_hash_table = HashTable()

my_hash_table.print_table()


"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""