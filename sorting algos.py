#### bubble sort
#always 'bubble' the larger number 2 the right as you go through the list
#O(n^2)

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
#O(n^2)

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

### binary Search
# divide and conquer
# keep spliting the arr in half until you find the number if it exisits
#look at each endpoint and find the mid point
#compare the midpoint to target num
#only keep the half that contains the target
#perform again and again until you find the target
## log(n)

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while (left <= right):
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#print(binarySearch([1,2,3,4,5,6,7,8,9,10,11], 3))
#print(binarySearch([1,2,3,4,5,6,7,8,9,10,11], 9))
#print(binarySearch([1,2,3,4,5,6,7,8,9,10], 11))

### merge sort
# similar to binary search but for sorting
# nlog(n)
# very similar to built in .sort()

def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # recursivly call each half
        mergeSort(left)
        mergeSort(right)


        # iterators for transversing the 2 halves
        i = 0
        j = 0

        # iterator for the main list
        k = 0

        # compare the left and right values
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # put the remaining values into the list
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        
        return arr

print(mergeSort([1,7,2,5,4,8,6,3,9,10]))


#recursion
def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num - 1)

# print(factorial(5))


