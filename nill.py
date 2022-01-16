#function that when given a list of email address returns the list without dupes

#multiple files with 1000 or so emails

def emailNoDupes(alist):
    if isinstance(alist, list):
        return set(alist)
    else:
       raise TypeError()

print(emailNoDupes(['1@gmail.com','1@gmail.com' ]))


def emailNoDupes2(emails1,emails2,emails3,emails4):

#-->input email list1
#--> additional lists
#-->take email1 from list 1
#--> check if email1 is in list1, if it is delete the dupe
#--> check if email1 is in list2, if it is delete the dupe 
#--> check if email1 is in list3

    emailCheck = emails1[0]
    i = 0

    while i < range(len(emails1)):
        if emails1.count(emailCheck) > 1:
            emails1.remove(emailCheck)
        elif emails2.count(emailCheck) > 0:
            emails2.remove(emailCheck)
        elif emails3.count(emailCheck) > 0:
            emails3.remove(emailCheck)
        elif emails4.count(emailCheck) > 0:
            emails4.remove(emailCheck)
        else:
            i += 1
            emailCheck = emails1[i]
    

    emailCheck = emails2[0]
    i = 0
    while i < range(len(emails2)):
        if emails2.count(emailCheck) > 1:
            emails2.remove(emailCheck)
        elif emails1.count(emailCheck) > 0:
            emails1.remove(emailCheck)
        elif emails3.count(emailCheck) > 0:
            emails3.remove(emailCheck)
        elif emails4.count(emailCheck) > 0:
            emails4.remove(emailCheck)
        else:
            i += 1
            emailCheck = emails2[i]

    
    