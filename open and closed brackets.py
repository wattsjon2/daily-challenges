#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#1. Open brackets must be closed by the same type of brackets.
#2. Open brackets must be closed in the correct order.
#Examples:
#Input: s = "()"
#Output: true
#Input: s = "()[]{}"
#Output: true
#Input: s = "(]"
#Output: false

def bracketCheck(string):
    checkDict = {'(':')',
                ')':'(',
                '[':']',
                ']':'[',
                '{':'}',
                '}':'{'
                }
    openClosed = 'closed'            
    for i in range(len(string)):
        if openClosed == 'closed':
            bracketCheck = string[i]
            openClosed = 'open'
        elif openClosed == 'open' and checkDict[string[i]] == bracketCheck:
            openClosed = 'closed'
        else:
            return False  
    return True

#print(bracketCheck("()[]{}"))
#print(bracketCheck("(]"))


def bracketCheck2(string):
    checkDict = {'(':')',
                '[':']',
                '{':'}',
                }

    while string != '':
        if len(string) == 1:
            return False
        elif string[0] not in checkDict:
            return False
        elif string[1] == checkDict[string[0]]:
            string = string[2:]
        else:
            return False
    return True

#print(bracketCheck2("()[]{}"))
#print(bracketCheck2("(]"))
#print(bracketCheck2("]("))
#print(bracketCheck2("()[]"))
#print(bracketCheck2("()[]("))
#print(bracketCheck2("()[](]"))

def bracketCheck3(string):
    checkDictOpen = {'(':')',
                '[':']',
                '{':'}',
                }

    posCount = 0


    while string != '':
        if len(string) == 1:
            return False
        elif string[0] not in checkDictOpen:
            return False
        elif string[posCount] in checkDictOpen and string[posCount + 1] in checkDictOpen:
            posCount += 1
        elif string[posCount] in checkDictOpen and string[posCount + 1] == checkDictOpen[string[posCount]]:
            string = string[:posCount] + string[posCount + 2: ]
            posCount = 0
        else:
            return False

    return True

print(bracketCheck3("()[]{}"))
print(bracketCheck3("(]"))
print(bracketCheck3("([{}])"))
print(bracketCheck2('({(}))'))
#print(bracketCheck2("()[]("))
#print(bracketCheck2("()[](]"))