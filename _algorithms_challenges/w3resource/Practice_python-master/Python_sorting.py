import copy





# 1 and 3
def binary_search(sorted_lists, num):
    """does a binary search on a given list for a given number
    (Binart search devides the list in half sees if number is smaller or bigger
    thencuts the other side off and devides. Olny works for a sorted list)
    """
    devided_list = sorted_lists
    mid = 0
    low = 0
    high = len(lists) - 1
    for x in range(len(devided_list)):
        high = len(devided_list) - 1
        try:
            mid = int((low + high) / 2)
        except isinstance((low + high) / 2, int) == False:
            mid = int(((low + high) / 2) - .5)

        if devided_list[mid] == num:
            return True
        elif devided_list[mid] < num:
            devided_list = devided_list[mid:]
        elif devided_list[mid] > num:
            devided_list = devided_list[:mid+1]
        else:
            return False
    else:
        return False


# print(binary_search([1,2,3,5,8], 10))
# print(binary_search([1,2,3,5,8], 5))


# 2
def sequential_search(lists, num):
    """finds an item in a given list through a sequesntial search """
    for key, item in enumerate(lists):
        if item == num:
            return (True, key)
    return False


# print(sequential_search([11,23,58,31,56,77,43,12,65,19],77))
# print(sequential_search([11,23,58,31,56,77,43,12,65,19],21))



# 4
def bubble_sort(lists):
    """sorts a list by bubble sorting which is pairing each one with its friend
    and changing them putting the higher one above and lower below
    """
    devided_list = lists
    unsorted = True
    while unsorted:
        unsorted = False
        for key, items in enumerate(devided_list):
            try:
                if items > devided_list[key + 1]:
                    devided_list[key] = devided_list[key + 1]
                    devided_list[key + 1] = items
                    unsorted = True
            except IndexError:
                pass
    return devided_list


# print(bubble_sort([14,46,43,27,57,41,45,21,70]))


# 5
def selection_sort(lists):
    """ uses selcetion sorting to sort a list.
    It loops through the listX^2 times checking each time what number is the
    smallest and appends it and puts it in a new list.
    """
    devided_list = lists
    sorted_list = []
    for x in range(len(lists)):
        smallest = 500000000000000
        for key, item in enumerate(devided_list):
            if item < smallest:
                smallest = item
        sorted_list.append(smallest)
        devided_list.remove(smallest)
    return sorted_list

# print(selection_sort([14,46,43,27,57, 70,41,45,21,70]))


# 6
def insertion_sorter(unsorted_list):
    """ Sorts a list with insertion sorting."""
    sorted_list = copy.deepcopy(unsorted_list[0:1])
    for item in unsorted_list[1:]:
        for sorted_item in sorted_list[::-1]:
            if item > sorted_item:
                sorted_list.insert(sorted_list.index(sorted_item) + 1, item)
                break
    return sorted_list


# print(insertion_sorter([14,46,43,27,57,41,45,21,70]))


# 7 needs to be fixed to go over each item
def shell_sorter(unsorted_list):
    """sorts a list through shell sorting which compare items in list by n gaps
    starting as n =  len(list) / 2 then n = n/2 till n=1. Then istays on 1
    which is bubble sort """
    gap = len(unsorted_list)
    print(unsorted_list)
    while gap > 2:
        last = 1
        gap = int(gap / 2)
        print(gap)
        for key, item in enumerate(unsorted_list[gap:]):
            if item < unsorted_list[key]:
                bigger_key = key + gap
                item2= unsorted_list.pop(bigger_key)
                unsorted_list.insert(key, item2)
                item1 = unsorted_list.pop(key+1)
                unsorted_list.insert(bigger_key, item1)
    return bubble_sort(unsorted_list)

# print(shell_sorter([14,46,43,27,57,41,45,21,70]))


# 8
def merge_sorter(unsorted_list):
    """ merge sort """
    sorted_list = []
    for num in unsorted_list:
        sorted_list.append([num])
    print(sorted_list)
    while len(sorted_list) > 1:
        next_list = []
        for key, value in enumerate(sorted_list[::2]):
            key = key * 2
            new_list = []
            try:
                list2 = sorted_list[key+1]
            except IndexError:
                list2 = []
            while True:
                if len(list2) > 0 and len(value) > 0:
                    # v
                    if list2[0] < value[0]:
                        num = sorted_list[key+1].pop(0)
                        new_list.append(num)
                    else:
                        num = sorted_list[key].pop(0)
                        new_list.append(num)
                elif len(list2) > 0:
                    # 
                    num = sorted_list[key+1].pop(0)
                    new_list.append(num)
                elif len(value) > 0:
                    # 
                    num = sorted_list[key].pop(0)
                    new_list.append(num)
                else:
                    next_list.append(new_list)
                    break
        sorted_list = next_list
        print(sorted_list)
        print(len(sorted_list))
    return sorted_list

# print(merge_sorter([14,46,43,27,57,41,45,21,3]))


# 9
def quick_sorter(unsorted_list):
    sorted_list = []
    index = 0
    nuzz = 0
    direction = "more"
    pivot = unsorted_list[nuzz]
    print(pivot)
    while True:
        if direction == "less":
            for key, value in enumerate(unsorted_list):
                if nuzz == key:
                    # end  comapasion when comapred number is same as pivot
                    sorted_list = [unsorted_list[:key], [pivot], unsorted_list[key+1:]]
                    return sorted_list
                elif pivot < value:
                    # changes position of pivot when pivot is less then number
                    bigger_num = unsorted_list.pop(key)
                    del unsorted_list[nuzz-1]
                    unsorted_list.insert(nuzz, bigger_num)
                    unsorted_list.insert(key, pivot)
                    nuzz = key
                    direction = "more"
                    break
        elif direction == "more":
            for key, value in enumerate(unsorted_list[::-1]):
                key = len(unsorted_list) - (key) - 1
                if nuzz == key:
                    # end  comapasion when comapred number is same as pivot
                    sorted_list = [unsorted_list[:key], [pivot], unsorted_list[key+1:]]
                    return sorted_list
                elif pivot > value:
                    # changes position of pivot when pivot is less then number
                    bigger_num = unsorted_list.pop(key)
                    del unsorted_list[nuzz]
                    if len(unsorted_list) - 1 == key:
                        unsorted_list.append(pivot)
                    else:
                        unsorted_list.insert(key-1, pivot)
                    unsorted_list.insert(nuzz, bigger_num)
                    nuzz = key
                    direction = "less"
                    break


"""def quick_check(sorted_list):
    unsorted = False
    new_list = []
    while unsorted == False:
        for index, lists in enumerate(sorted_list):
            unsorted = True
            print(lists)
            if len(lists) > 1:
                sortedl = quick_sorter(lists)
                sorted_list.insert(index, sortedl)
                print(sorted_list)
                unsorted = False
            else:
                
            
    return sorted_list"""

# print(quick_sorter([5,2,6,1,3,4]))



def counting_sorter(unsorted_list):
    """ sorts the list through counting sort meaning makes a dict of every
    number between the smallest and largest number as a key and value is a
    the times number is in unsorted_list
    """
    sorted_list = []
    maxs = -10000000000000000000000
    mins = 100000000000000000000000
    for num in unsorted_list:
        if num < mins:
            mins = num
        if num > maxs:
            maxs = num
    num_dict = {num:0 for num in range(mins, maxs+1)}
    print(num_dict)
    for num in unsorted_list:
        if num in num_dict:
            num_dict[num] += 1
    print(num_dict)
    for num in num_dict:
        for mun in range(0,num_dict[num]):
            sorted_list.append(num)
    return sorted_list


print(counting_sorter([9,4,10,8,2,4]))





