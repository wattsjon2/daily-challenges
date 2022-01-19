#### bubble sort
#always 'bubble' the larger number 2 the right as you go through the list

def bubbleSort(alist):
    isSorted = False
    sortedNums = 0

    while isSorted == False:
        isSorted = True
        for i in range(len(alist) - sortedNums - 1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                isSorted = False
        sortedNums += 1
    return alist

#print(bubbleSort([3,2,1]))
#print(bubbleSort([1,5,3,2,4]))
#print(bubbleSort([5,3,2,1,4]))

#### insertion sort

#loop over array
#check a value at an index vs all values before it

def insertionSort(alist):
    for i in range(1, len(alist)):
        j = i
        while j > 0:
            if alist[j] < alist[j - 1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                j -= 1
            else:
                break
    return alist

#print(insertionSort([1,5,3,2,4]))
        

