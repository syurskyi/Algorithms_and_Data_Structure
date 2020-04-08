class BubbleArray(list):
    def __init__(self, *args, **kwargs):
        self.swap_ptr = None
        super(BubbleArray, self).__init__(*args, **kwargs)
        
    def __repr__(self):
        if self.swap_ptr is None:
            return "(" + " ".join([str(value) for value in self]) + ")"
        else:
            return "(" + " ".join(
                ['\033[1m' + str(value) if i == self.swap_ptr - 1
                 else str(value) + '\033[0m' if i == self.swap_ptr
                 else str(value) for i, value in enumerate(self)]) + ")"  
        

def swap(array: BubbleArray, i: int, j: int) -> None:
    buff = array[i]
    array[i] = array[j]
    array[j] = buff

    
def bubble_sort(array: BubbleArray, show_wasted: bool=False) -> None:
    n = len(array)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if array[i-1] > array[i]:
                if isinstance(array, BubbleArray):
                    array.swap_ptr = i
                    print(array, end='')
                swap(array, i-1, i)
                if isinstance(array, BubbleArray):
                    print(" ->", array)
                swapped = True
            else:
                if show_wasted:
                    array.swap_ptr = None
                    print("\033[91m" + str(array), "->", str(array) + "\033[0m")
        n -= 1
        
        
def bubble_sort_improved(array: BubbleArray, show_wasted: bool=False) -> None:
    n = len(array)
    while n > 1:
        newn = 1
        for i in range(1, n):
            if array[i-1] > array[i]:
                if isinstance(array, BubbleArray):
                    array.swap_ptr = i
                    print(array, end='')
                swap(array, i-1, i)
                if isinstance(array, BubbleArray):
                    print(" ->", array)
                newn = i
            else:
                if show_wasted:
                    array.swap_ptr = None
                    print("\033[91m" + str(array), "->", str(array) + "\033[0m")
        n = newn
