#Check for Unique Emails:
#Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails. You can assume each string in the array is a valid email address.
#Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
#For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
#If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
#For example, "alice.z@leetcode.com" and "alicez@leetcode.com"forward to the same email address.
#If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
#For example, "m.y+name@email.com" will be forwarded to "my@email.com".
#It is possible to use both of these rules at the same time.
#10:00
#Example 1:
#Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#Output: 2
#Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
#Example 2:
#Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
#Output: 3
#HINT: This is much simpler than it looks.


def uniqueEmails(alist):
    newSet = set()
    for email in alist:
        i = 0
        plus = 0
        while i < len(email):
           
            if email[i] == "@" and plus == 0:
                break
            elif email[i] == "@":
                email = email[:plus] + email[i:]
                break
            elif email[i] == "." and plus == 0:
                email = email[:i] + email[i+1:]
            elif email[i] == "+":
                plus = i
                i += 1
            else:
                i += 1
        newSet.add(email)
        

    return len(newSet)

print(uniqueEmails(["tes.t@gmail.com","test@gmail.com", "test+test@gmail.com"]))
                
                

