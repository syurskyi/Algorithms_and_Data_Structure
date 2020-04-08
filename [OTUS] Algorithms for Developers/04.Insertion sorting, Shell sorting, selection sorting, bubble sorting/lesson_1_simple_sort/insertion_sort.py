class InsertionArray(list):
    def __init__(self, *args, **kwargs):
        self.swap_ptr = None
        self.min_ptr = None
        super(InsertionArray, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        if self.swap_ptr is None and self.min_ptr is None:
            return "(" + " ".join([str(value) for value in self]) + ")"
        else:
            return "(" + " ".join( 
                ['\033[1m\033[92m'] + [
                    '\033[0m\033[1m' + str(value) + '\033[0m' if i == self.min_ptr
                    else str(value)
                    for i, value in enumerate(self)]) + ")"  
        

def swap(array: InsertionArray, i: int, j: int) -> None:
    buff = array[i]
    array[i] = array[j]
    array[j] = buff

    
def insertion_sort(array: InsertionArray) -> None:
    for i in range(1, len(array)):
        if isinstance(array, InsertionArray):
            array.min_ptr = i
        j = i        
        while j > 0 and array[j-1] > array[j]:
            if isinstance(array, InsertionArray):
                array.swap_ptr = j
                print(array)

            swap(array, j, j-1)
            j -= 1
