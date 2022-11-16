#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

import math

___ bubbleSort(customList
    ___ i __ r..(l..(customList)-1
        ___ j __ r..(l..(customList)-i-1
            __ customList[j] > customList[j+1]:
                customList[j], customList[j+1] _ customList[j+1], customList[j]
    print(customList)


___ selectionSort(customList
    ___ i __ r..(l..(customList
        min_index _ i
        ___ j __ r..(i+1, l..(customList
            __ customList[min_index] > customList[j]:
                min_index _ j
        customList[i], customList[min_index] _ customList[min_index], customList[i]
    print(customList)

___ insertionSort(customList
    ___ i __ r..(1, l..(customList
        key _ customList[i]
        j _ i-1
        _____ j>_0 ___ key < customList[j]:
            customList[j+1] _ customList[j]
            j -_ 1
        customList[j+1] _ key
    r_ customList


___ bucketSort(customList
    numberofBuckets _ round(math.sqrt(l..(customList)))
    maxValue _ m__(customList)
    arr _    # list

    ___ i __ r..(numberofBuckets
        arr.a..(   # list)
    ___ j __ customList:
        index_b _ math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].a..(j)
    
    ___ i __ r..(numberofBuckets
        arr[i] _ insertionSort(arr[i])
    
    k _ 0
    ___ i __ r..(numberofBuckets
        ___ j __ r..(l..(arr[i]
            customList[k] _ arr[i][j]
            k +_ 1
    r_ customList

___ merge(customList, l, m, r
    n1 _ m - l + 1
    n2 _ r - m

    L _ [0] * (n1)
    R _ [0] * (n2)

    ___ i __ r..(0, n1
        L[i] _ customList[l+i]
    
    ___ j __ r..(0, n2
        R[j] _ customList[m+1+j]
    
    i _ 0
    j _ 0
    k _ l
    _____ i < n1 ___ j < n2:
        __ L[i] <_ R[j]:
            customList[k] _ L[i]
            i +_ 1
        ____
            customList[k] _ R[j]
            j +_ 1
        k +_ 1
    _____ i < n1:
        customList[k] _ L[i]
        i +_ 1
        k +_ 1
    
    _____ j < n2:
        customList[k] _ R[j]
        j +_ 1
        k +_ 1

___ mergeSort(customList, l, r
    __ l < r:
        m _ (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
    r_ customList

___ partition(customList, low, high
    i _ low - 1
    pivot _ customList[high]
    ___ j __ r..(low,high
        __ customList[j] <_ pivot:
            i +_ 1
            customList[i], customList[j] _ customList[j], customList[i]
    customList[i+1], customList[high] _ customList[high], customList[i+1]
    r_ (i+1)

___ quickSort(customList, low, high
    __ low < high:
        pi _ partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)


___ heapify(customList, n, i
    smallest _ i
    l _ 2*i + 1
    r _ 2*i + 2
    __ l < n ___ customList[l] < customList[smallest]:
        smallest _ l
    
    __ r < n ___ customList[r] < customList[smallest]:
        smallest _ r
    
    __ smallest !_ i:
        customList[i], customList[smallest] _ customList[smallest], customList[i]
        heapify(customList, n, smallest)


___ heapSort(customList
    n _ l..(customList)
    ___ i __ r..(i..(n/2)-1, -1, -1
        heapify(customList, n, i)
    
    ___ i __ r..(n-1,0,-1
        customList[i], customList[0] _ customList[0], customList[i]
        heapify(customList, i, 0)
    # customList.reverse()



cList _ [2,1,7,6,5,3,4,9,8]
heapSort(cList)
print(cList)




        