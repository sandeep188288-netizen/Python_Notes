#INHERITANCE
"""
1. Single Inheritance -> 1 Parent class and 1 Child Class
2. Multiple Inheritance -> 2 Parent class and 1 Child Class
3. Multilevel Inheritance -> One child becomes Parent of another class
4. Hierarchial Inheritance -> 1 Parnet and multiple child
5. Hybrid Inheritance -> Combination of 2 types of inheritance
"""
#1. Single Inheritance
"""class Parent:
    def _init_(self):
        print('This is Parent class constructor')

    def greet(self):
        print('This is Parent class')

class Child(Parent):
    def _init_(self):
        print("This is child class constructor")

    def show(self):
        print('This is Child class')


obj = Child()
obj.greet()
obj.show()
"""

"""class Factory:
    def _init_(self,name,color):
        self.name = name
        self.color = color
    
    def show(self):
        print(f'Bag has {self.name} and {self.color} color')
    
class Bata(Factory):
    def _init_(self,name,color,zip,pockets):
        super()._init_(name,color)
        self.zip = zip
        self.pockets = pockets
    
    def display(self):
        print(f'Bag has {self.name} , {self.color} color , {self.zip} zip and {self.pockets} pockets')
Rahul = Bata('Rahul','Purple',4,10)
Rahul.display()"""


"""
#2. Multiple Inheritane -> 2 Parent, 1 Child
class Father: #Parent1

    def _init_(self):
        print('This is Father class constructor')

    def greet_father(self):
        print('This is Father class')

class Mother: #Parent2
    def _init_(self):
        print('This is Mother class constructor')

    def greet_mother(self):
        print('This is Mother class')


class Child(Mother,Father): #Child
    #If we have to run constructor of Father class first
    
    def _init_(self):
        Father._init_(self) #Sabse pehle Father class ka constructor will be run
        Mother._init_(self) #After Father class Mother class constructor will be run

obj = Child()
obj.greet_father()
obj.greet_mother()
"""



#Multilevel Inheritance -> One Child class becomes Parent of another class
"""
EX:1
class A: #Parent class
    def greet(self):
        print("This is Class A")

class B(A): #Child Class
    def show(self):
        print('This is Class B')

class C(B):
    def details(self):
        print("This is Class C")

obj = C()
obj.show()
obj.greet()
obj.details()

EX:2
class CEO: #Super Parent
    def _init_(self):
        print("This is CEO class constructor")
    
class Manager(CEO): #Child class,Parent
    def _init_(self):
        super()._init_()
        print('This is Manager class Constructor')
    
class Employee(Manager):#child
    def _init_(self):
        super()._init_()
        print('This is Employee class constructor')

rahul = Employee()
"""



#Hierarchial Inheritance
"""
EX:1
class Parent:
    def greet(self):
        print("This is Parent class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj = Child2()
obj.greet()

obj2 = Child1()
obj2.greet()

EX:2
class Account:
    def _init_(self,name,balance):
        self.name = name
        self.balance = balance
    
    def details(self):
        print(f"Hello {self.name} you have {self.balance}")
    
class Saving(Account):
    def _init_(self,name,balance):
        super()._init_(name,balance)
        print(f'This is Saving class constructor {self.name} , {self.balance}')

class Current(Account):
    def _init_(self,name,balance,type):
        super()._init_(name,balance)
        self.type = type
        print(f'This is Current class Constructor {self.name} , {self.balance}, {self.type}')

obj = Current("Mukesh",0,"Current")
"""
