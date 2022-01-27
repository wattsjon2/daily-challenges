#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
#Example 1:
#Input: s = "hello"
#Output: "holle"
#Example 2:
#Input: s = "leetcode"
#Output: "leotcede"

def reverseVowels(string):
    vowelList = []
    vowelSet = {"a", "e", "i", "o", "u"}

    for letter in string:
        if letter in vowelSet:
            vowelList.append(letter)

    for i in range(len(string)):
        if string[i] in vowelSet:
            string = string[:i] + vowelList.pop(-1) + string[i+1:]
    
    return string

print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
