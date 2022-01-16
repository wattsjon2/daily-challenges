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

print(longestSubString("abcabcbb"))
print(longestSubString("bbbbb"))
print(longestSubString("pwwkew"))
print(longestSubString("abcd"))
print(longestSubString("aabcd"))


