#1. Arithematic operators(+, -, /, *, //, **, %)
#2.Assignment operator()
#3. comparison operators
#4.Logical operators

a = 12
b = 5
#print(int(a/b)) 

#print(a // b)     #floor division give int value

#print(5 ** 2)        #power 5^2

#print(a ** b)

#rint(a % b)           #mod

#BODMAS


p = float(input("enter priciple: "))
r = float(input("enter rate: "))
t = float(input("enter time: "))

#si = (p*r*t)/100
ci = p*(1+(r/100))**t
#ci = amount - p 
#print(f"your simple interest will be {ci}")
print(f"your compound interest will be {ci - p}")