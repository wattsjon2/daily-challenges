#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"while "aec" is not).
#Example 1:
#Input: s = "abc", t = "ahbgdc"
#Output: true
#Example 2:
#Input: s = "axc", t = "ahbgdc"
#Output: false

def subStringCheck(s,t):
    sEnumDict = {}
    sSet = set()
    checkDict = {}
    counter = 0
    for i, j in enumerate(s):
        sEnumDict[i] = j
        sSet.add(j)

    for letter in t:
        if letter in sSet:
            checkDict[counter] = letter
            counter += 1
    
    return checkDict == sEnumDict


print(subStringCheck("abc","ahbgdc"))
print(subStringCheck("axc","ahbgdc"))
