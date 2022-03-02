#You are given a string s representing an attendance record for a Coding Temple student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
#'A': Absent.
#'L': Late.
#'P': Present.
#The student is eligible for an attendance award if they meet both of the following criteria:
#The student was absent ('A') for strictly fewer than 2 days total.
#The student was never late ('L') for 3 or more consecutive days.
#Return true if the student is eligible for an attendance award, or false otherwise.
#Example 1:
#Input: s = "PPALLP"
#Output: true
#Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
#Example 2:
#Input: s = "PPALLL"
#Output: false
#Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

def award(string):
    if string.count("A") > 1:
        return False

    if string.count("LLL") > 0:
        return False

    return True


print(award("PPLALP"))
print(award("PPALLL"))
print(award("PPLAPLL"))

def award2(string):
    return string.count("A") < 2 and string.count("LLL") < 1

print(award2("PPLALP"))
print(award2("PPALLL"))
print(award2("PPLAPLL"))
