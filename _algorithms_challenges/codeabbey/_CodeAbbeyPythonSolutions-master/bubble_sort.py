amount_values = int(input())

def get_pass_and_swap_number(array):
    passed = 0
    swapped = 0

    n = len(array)
    for i in range(n):
        previous_swap = swapped
        for j in range(n-i-1):
            if(array[j] > array[j+1]):
                swapped += 1
                array[j], array[j+1] = array[j+1], array[j]
        passed += 1

        if(previous_swap == swapped):
            break  
    

    print (passed, swapped)

array = list(map(int, input().split()))
get_pass_and_swap_number(array)