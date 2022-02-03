#Extremely delayed challenge today... but here it is! Will be giving out the answer first thing tomorrow morning!
#Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
#Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#a, b are from arr
#a < b
#b - a equals to the minimum absolute difference of any two elements in arr
 
#Example 1:
#Input: arr = [4,2,1,3]
#Output: [[1,2],[2,3],[3,4]]
#Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
#Example 2:
#Input: arr = [1,3,6,10,15]
#Output: [[1,3]]
#Example 3:
#Input: arr = [3,8,-10,23,19,-4,-14,27]
#Output: [[-14,-10],[19,23],[23,27]]

def minAbsDiff(arr):
    arr.sort()
    pairsArr = []
    minAbs = abs(arr[1] - arr[0])
    pairsMin = []

    for i in range(len(arr) -1):
        pairsArr.append([arr[i],arr[i+1]])
        if abs(arr[i+1] - arr[i]) < minAbs:
            minAbs = abs(arr[i+1] - arr[i])
    for pair in pairsArr:
        if abs(pair[1] - pair[0]) == minAbs:
            pairsMin.append(pair)
    return pairsMin


print(minAbsDiff([4,2,1,3]))
print(minAbsDiff([1,3,6,10,15]))
print(minAbsDiff([3,8,-10,23,19,-4,-14,27]))