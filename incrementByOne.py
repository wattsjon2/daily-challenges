#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.
#Example 1:
#Input: digits = [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Incrementing by one gives 123 + 1 = 124.
#Thus, the result should be [1,2,4].
#Example 2:
#Input: digits = [4,3,2,1]
#Output: [4,3,2,2]
#Explanation: The array represents the integer 4321.
#Incrementing by one gives 4321 + 1 = 4322.
#Thus, the result should be [4,3,2,2].
#Example 3:
#Input: digits = [9]
#Output: [1,0]
#Explanation: The array represents the integer 9.
#Incrementing by one gives 9 + 1 = 10.
#Thus, the result should be [1,0].

def incrementByOne(alist):
    if alist[len(alist) - 1] != 9:
        alist[len(alist) - 1] += 1

    else:
        indexCounter = 0
        while alist[len(alist) - 1 - indexCounter] == 9:
            if indexCounter + 1 == len(alist):
                alist[0] = 0
                alist.insert(0,1)

            elif alist[len(alist) - 1 - indexCounter] == 9 and alist[len(alist) - 2 - indexCounter] == 9:
                alist[len(alist) - 1 - indexCounter]  = 0
                indexCounter += 1
            else:
                alist[len(alist) - 1 - indexCounter]  = 0
                alist[len(alist) - 2 - indexCounter] += 1
                indexCounter += 1
    return alist



print(incrementByOne([1,2,3]))
print(incrementByOne([4,3,2,1]))
print(incrementByOne([9]))
print(incrementByOne([8,9]))
print(incrementByOne([9,9]))
print(incrementByOne([9,9,9,9,9]))