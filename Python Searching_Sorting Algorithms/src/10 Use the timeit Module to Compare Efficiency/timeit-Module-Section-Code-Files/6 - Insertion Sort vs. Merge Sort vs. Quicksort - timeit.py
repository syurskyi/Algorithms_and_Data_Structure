import timeit

NUM_REPETITIONS = 100

SETUP_CODE = "from random import shuffle"

# First test case - Insertion Sort

def insertion_sort(lst):
    for i in range(1, len(lst)):
        elem_selected = lst[i]

        while i > 0 and elem_selected < lst[i-1]:
            lst[i] = lst[i-1]
            i -= 1

        lst[i] = elem_selected


test_code_1 = '''

a = [i for i in range(1000)]

shuffle(a)

insertion_sort(a)

'''

print("\n==> Testing Insertion Sort")

time = timeit.timeit(test_code_1, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


# Second test case - Merge Sort

def merge_sort(lst):
    
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        middle_index = len(lst)//2

        left = merge_sort(lst[:middle_index])
        right = merge_sort(lst[middle_index:])

        return merge(left, right)


def merge(left_half, right_half):

    if not left_half or not right_half:
        return left_half or right_half
    
    result = []
    i, j = 0, 0

    while True:
        
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

        if i == len(left_half) or j == len(right_half):
            result.extend(left_half[i:] or right_half[j:])
            break

    return result


test_code_2 = '''

b = [i for i in range(1000)]

shuffle(b)

merge_sort(b)

'''

print("\n==> Testing Merge Sort")

time = timeit.timeit(test_code_2, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)


# Third test case - Quicksort

def quicksort(lst, low, high):
    if low < high: 
        pivot_index = partition(lst, low, high) 
   
        quicksort(lst, low, pivot_index-1) 
        quicksort(lst, pivot_index+1, high)

def partition(lst, low, high):
    pivot = lst[high]

    i = low - 1     
  
    for j in range(low, high): 
        if lst[j] <= pivot: 
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
             
    lst[i+1], lst[high] = lst[high], lst[i+1] 
    return i+1

test_code_3 = '''

c = [i for i in range(1000)]

shuffle(c)

quicksort(c, 0, len(c)-1)

'''

print("\n==> Testing Quicksort")

time = timeit.timeit(test_code_3, setup=SETUP_CODE, number=NUM_REPETITIONS, globals=globals())

print("Total time to sort the list:", time)
print("Average time per repetition:", time/NUM_REPETITIONS)
