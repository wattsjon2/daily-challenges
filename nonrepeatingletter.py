#Given a string s, find the first non-repeating character in it 
#and return its index. If it does not exist, return -1.
#Example 1:
#Input: s = "codingtemple"
#Output: 0
#Example 2:
#Input: s = "codingcodingalumni"
#Output: 12
#Example 3:
#Input: s = "ctct"
#Output: -1

def nonRepeatingLetter(s):
    letterDict = {}
    letterLoc = {}
    for i in range(len(s)):
        if s[i] not in letterLoc:
            letterLoc[s[i]] = i
    for letter in s:
        if letter not in letterDict:
            letterDict[letter] = 1
        else:
            letterDict[letter] = letterDict.get(letter) + 1

    for key,value in dict(letterDict).items():
        if value != 1:
            del letterDict[key]

    for key,value in dict(letterLoc).items():
        if key not in letterDict:
            del letterLoc[key]

    if letterLoc != {}:
        return min(letterLoc.items())[-1]
    else:
        return -1
    

print(nonRepeatingLetter("codingtemple"))
print(nonRepeatingLetter("codingcodingalumni"))
print(nonRepeatingLetter("ctct"))

def nonRepeatingLetter2(s):
    letterDict = {}
    letterLoc = {}
    for i in range(len(s)):
        if s[i] not in letterLoc:
            letterLoc[s[i]] = i
            letterDict[s[i]] = 1
        else:
            letterDict[s[i]] = letterDict.get(s[i]) + 1

    if min(letterDict.items())[-1] == 1:
        return min(letterLoc.items())[-1]
    else:
        return -1
    

print(nonRepeatingLetter2("codingtemple"))
print(nonRepeatingLetter2("codingcodingalumni"))
print(nonRepeatingLetter2("ctct"))


