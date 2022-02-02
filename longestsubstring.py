#Find the Longest Substring w/o Repeating Characters
#Given a string s, find the length of the longest substring without repeating characters.
#Examples:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def longestSubString(string):
    substring = set()
    substringList = []
    for letter in string:
        if letter not in substring:
            substring.add(letter)
        else:
            substringList.append(len(substring))
            substring = set(letter)
    
    substringList.append(len(substring))        
    return max(substringList)

#print(longestSubString("abcabcbb"))
#print(longestSubString("abcadbabb"))
#print(longestSubString("bbbbb"))
#print(longestSubString("pwwkew"))
#print(longestSubString("abcd"))
#print(longestSubString("aabcd"))

def longestSubString2(string):
    l = 0
    r = 0
    subString = set()
    longest = 0
    while r < len(string):
        if string[r] not in subString:
            longest = max(longest,r-l + 1)
            subString.add(string[r]) 

        else:
            longest = max(longest, r-l)
            l += 1

        if string[r] == string[r-1]:
            
            subString.clear
            subString.add(string[r])
            l += 1

        r += 1
    return longest

print(longestSubString2("abcabcbb"))        
print(longestSubString2("abcadbabb"))        
print(longestSubString2("pwwkew"))        

