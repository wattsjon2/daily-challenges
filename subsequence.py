#Given two non-empty arrays of integers(numbers), write a function that 
#determines whether the second array is a subsequence of the first one.
#A subsequence of an array is a set of numbers that aren’t necessarily 
#adjacent in the array but that are in the same order as they appear in 
#the array. For instance, the numbers [1,3,4] form a subsequence of the 
#array [1,2,3,4], and so do the numbers [2,4]. Note that a single number 
#in an array and the array itself are both valid subsequences of the array.
#( [1],[2],[3],[4]and [1,2,3,4] are all valid subsequences of [1,2,3,4] )
#Sample Output
#array = [5,1,22,25,6,-1,8,10]
#subsequence = [1,6,-1,10]
#Answer: True

def subsequence(arr1, arr2):
    arr1EnumDict = dict([(y,x) for x,y in enumerate(arr1)])
    orderCheck1 = ''

    for i in arr2:
        if i not in arr1EnumDict:
            return False
        if orderCheck1 != '':
            if orderCheck1 > arr1EnumDict.get(i):
                return False    
        orderCheck1 = arr1EnumDict.get(i)
    return True

print(subsequence([5,1,22,25,6,-1,8,10],[1,6,-1,10]))
print(subsequence([5,1,22,25,6,-1,8,10],[1,6,-1,11]))
print(subsequence([5,1,22,25,6,-1,8,10],[1,-1,6,10]))
