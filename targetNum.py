#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.
#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2
#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1
#Example 3:
#Input: nums = [1,3,5,6], target = 7
#Output: 4

def targetNum(nums, target):
    numsSet = set(nums)
    if target in numsSet:
        return nums.index(target)

    else: 
        if target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] < target:
                    pass
                else:
                    return i

print(targetNum([1,3,5,6],5))
print(targetNum([1,3,5,6],7))
print(targetNum([1,3,5,6],0))
print(targetNum([1,3,5,6],2))
print(targetNum([1,3,5,6],4))


def searchInsert(nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left