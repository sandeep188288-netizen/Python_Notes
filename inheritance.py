#INHERITANCE
"""
1. Single Inheritance -> 1 Parent class and 1 Child Class
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchial Inheritance
5. Hybrid Inheritance
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