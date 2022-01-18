#Write an algorithm to determine if a number n is happy.
#A happy number is a number defined by the following process:
#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.
#Input: n = 19
#Output: true
#Explanation:
#1**2 + 9**2 = 82
#8**2 + 2**2 = 68
#6**2 + 8**2 = 100
#1**2 + 0**2 + 0**2 = 1
#input: n = 2
#Output: false

def happyNums(n):
    newTot = 0
    answerSet = set()
    while n not in answerSet:
        for digit in str(n):
            newTot = int(digit)**2 + newTot
        answerSet.add(n)
        n = newTot
        newTot = 0
        if n == 1:
            return True  
    return False

print(happyNums(19))
print(happyNums(2))
        