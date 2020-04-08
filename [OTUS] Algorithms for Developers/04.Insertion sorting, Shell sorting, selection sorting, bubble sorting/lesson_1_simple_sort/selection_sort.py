class SelectionArray(list):
    def __init__(self, *args, **kwargs):
        self.swap_ptr = None
        self.min_ptr = None
        super(SelectionArray, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        if self.swap_ptr is None and self.min_ptr is None:
            return "(" + " ".join([str(value) for value in self]) + ")"
        else:
            return "(" + " ".join( 
                ['\033[1m' + str(value) + '\033[0m' if i == self.swap_ptr
                 else '\033[1m\033[91m' + str(value) + '\033[0m' if i == self.min_ptr 
                 else str(value)
                 for i, value in enumerate(self)]) + ")"  
        

def swap(array: SelectionArray, i: int, j: int) -> None:
    buff = array[i]
    array[i] = array[j]
    array[j] = buff

    
def selection_sort(array: SelectionArray) -> None:
    n = len(array)
    for j in range(n-1):
        print("select")
        if isinstance(array, SelectionArray):
            array.swap_ptr = j
        idx_min = j
        if isinstance(array, SelectionArray):
            array.min_ptr = idx_min
        for i in range(j+1, n):
            if array[i] < array[idx_min]:
                idx_min = i;
                if isinstance(array, SelectionArray):
                    array.min_ptr = idx_min
            if isinstance(array, SelectionArray):
                print(array)
        if idx_min != j:
            swap(array, j, idx_min)
            if isinstance(array, SelectionArray):
                print("swap\n{}".format(array))
