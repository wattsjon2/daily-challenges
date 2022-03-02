#Given two strings ransomNote and magazine, return true if ransomNotecan be constructed from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.
#Example 1:
#Input: ransomNote = "a", magazine = "b"
#Output: false
#Example 2:
#Input: ransomNote = "aa", magazine = "ab"
#Output: false
#Example 3:
#Input: ransomNote = "aa", magazine = "aab"
#Output: true

def ransomNote(ransomNote, magazine):
    magazineDict = {}
    for letter in magazine:
        if letter in magazineDict:
            magazineDict[letter] += 1
        else:
            magazineDict[letter] = 1

    for letter in ransomNote:
        if letter not in magazineDict:
            return False

        else:
            if magazineDict[letter] > 1:
                magazineDict[letter] -= 1
            else:
                del magazineDict[letter]

    return True

print(ransomNote("a","b"))
print(ransomNote("aa","ab"))
print(ransomNote("aa","aab"))
