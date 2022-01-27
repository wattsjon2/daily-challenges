from multiprocessing.connection import wait


def findWaitTime(arr):
    arr.sort()
    waitTime = [0]
    for i in range(len(arr)):
        if i == 0 :
            pass
        else:
            waitTime.append(arr[i-1] + waitTime[i - 1])
    return sum(waitTime)
        


print(findWaitTime([1,3,2,1,6,7]))
print(findWaitTime([1,2,4,5,2,1]))
