class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
        


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  [['bolts', 1400], ['washers', 50]]
    5 :  None
    6 :  [['lumber', 70]]

"""