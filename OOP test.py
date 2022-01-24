class Person:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def __init__(self, name, age):   # this does not work like java
        self.name =  name
        self.age = "12"



P1 = Person("John", "15")
#P2 = Person("Jill") 

print(P1.name + " " + P1.age)
#print(P2.name + " " + P2.age)

#class Person2:
#    __name = ""
#    __age  = ""#
#
#    def persons(name, age):
#        __name = name
#        __age = age

#    def getName():
#        return __name


    