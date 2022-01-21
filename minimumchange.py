from cgi import test


def minChange(alist):
    if alist == []:
        return 1
    alist.sort()
    sumSet = set()
    for i in range(len(alist)):
        for j in range(len(alist)):
            if i == j:
                sumSet.add(alist[i])
            elif j < i:
                pass
            elif j + 1 == len(alist):
                sumSet.add(sum(alist[i:]))
                print("test")
            else:
                sumSet.add(sum(alist[i:j+1]))

    print(sumSet)

    testNum = 1
    for num in sumSet:
        if num == testNum:
            testNum += 1
        else:
            return testNum
    return testNum



print(minChange([1,2,3,4]))

def minChange2(coins):
    coins.sort()
    current_seen = 0
    for coin in coins:
        if coin > current_seen + 1:
            return current_seen + 1
        else:
            current_seen += coin

    return current_seen + 1

#print(minChange2([1,2,3,4]))

