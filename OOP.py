# CLASS
'''class SharmaVishnu:
    a = "riju"  # class k andarr variable -> attributes
    def sample():
        print("this is sample function")

SharmaVishnu.sample()
print(SharmaVishnu.a)'''

#-------------------------------------------------

# OBJECT

# class Animal:
#     name = "Animal"     # Attributes

#     # Method
#     def greet(self):    #jab bhi ek class k andarr ke function ko object ki help se call karoge 
#                         # to ek PARAMETER set karna hoga
#         print("this is aanimal class")

#     hello = Animal()  #here var is object
#     # variable k andarr class rakh do object bann ajega
#     # object and varible ka name same hota hai
#     hello.greet()
#     print(hello.name)

# class Animal:
#     name = "Animal"   # Attribute

#     def greet(self):  # Method
#         print("this is animal class")


# # Object creation (class ke bahar)
# hello = Animal()

# # Method call
# hello.greet()

# # Attribute access
# print(hello.name)


'''
class greet:
    def greet1(self):       #instead of self write anything
        print("hello")

    def add(self):
        a = 10
        b = 20
        print("sum:", a+b)

obj = greet()
obj.greet1()
obj.add()

'''

#-----------------------------------------------

# if two function with same name inside a single class then the latest one will be executable
    
# CONSTRUCTOR
# constructor sabse pehle execute hone wale function hai,
# doe'nt matter uske uprr aur neeche kon sa function hai

'''
class sharma:
    def greet(self):
        print("this is greet function")

    def __init__(self):
        print("this is constructor function")

obj = sharma()
obj.greet()
'''

#---------------------------------------------------

'''class sharma:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("this is constructor function")

    def menu(self):
        print(self.name)
        print(self.age)
        print("hello")

obj = sharma("sandeep",21)
obj.menu()'''
'''
class number:
    def __init__(self,n1,n2):
        self.n1 = n1        # instance attribute
        self.n2 = n2        # instance attribute
        print("this is constructor function")

    def menu(self):
        if self.n1 > self.n2:
            print("n1 is greater")
        else:
            print("n2 is greater")

obj = number(40,20)
obj.menu()

'''

#-----------------------------------------------------

#1.classmethod
#2.staticmethod

#1.classmethod
# class k instance and attributes
#  object k instance and attributes se change nahi ho sakte
# class Animal:
#     name = "Dog"

#     def change(self, new):
#         self.name = new
#         print(self.name)

# cheeta = Animal()
# cheeta.change("cat")
# print(Animal.name)
#----------------------------------------

#below class method class k attributs ko change karr skta hai bas
# class Animal:
#     name = "Dog"

#     @classmethod
#     def change(cls, new):
#         cls.name = new
#         print(cls.name)

# cheeta = Animal()
# cheeta.change("cat")
# print(Animal.name)
    
#------------------------------------------------------

# 2. staticmethod #independent of an object 
                  #no need to create a self inside function

class Vishnu:

    @staticmethod
    def menu():
        print("paneer")
        print("rajma")

new_market = Vishnu()
new_market.menu()
