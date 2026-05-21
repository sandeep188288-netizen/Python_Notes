# # ( ==, > , <, >=, <=, !=). -> they will always produce result in boolean

# # print(12 == 12.1)
# # print(12.2 > 12.1)

# # logical opertor(and, or, not)

# #AND
# print(12 == 12 and 33 == 33 and 12 > 10)
# #all these operation must be true 
# #if a single operation is false the final result will be false

# # OR
# print(12 > 34 or 13 > 45 or 56 == 78 or 12 == 12)
# #if any one of the operation is true the whole resullt will be true

# # NOT
# print(not 12 == 12)
# # converts true to false or false to true

# print(bool(0) and 12 == 12)


#CONTROL FLOW. -> (if else , loops , functions)

# age = int(input("Enter your age ! : "))

# if age >= 18:
#     print("You can vote")

# else:
#     print("You cannot vote")

# a)10 b)20 c)30 d)40

# ans = input("please select your option (a,b,c,d) ")

# if ans == "a":
#     print("10 is wrong answer")

# elif ans == "b":
#     print("20 is wrong answer")

# elif ans == "c":
#     print("30 is wrong answer")

# else:
#     print("40 is right answer")

# Q1----------------------------------
# a = int(input("enter value of a : "))
# b = int(input("enter value of b : "))

# if a > b:
#     print("a is geater")

# elif a==b:
#     print("a is equal to b")

# else:
#     print("b is greater")

# Q2----------------------------------
# gen = input("enter your gender as char (M or F): ")

# if gen == "M" or gen == "m":
#     print("good morning sir")

# elif gen == "F" or gen == "f":
#     print("good morning ma'am")

# else:
#     print("unknown gender")

# Q3----------------------------------

# num = int(input("enter a number : "))

# if num%2 == 0:
#     print("number is even number")

# else:
#     print("number is odd number")

# Q4----------------------------------
# name = input("enter your name : ")
# age = int(input("Enter your age ! : "))

# if age >= 18:
#     print(f"{name} you are valid voter")

# else:
#     print(f"{name} you are not a valid voter, you can vote after {18 - age} years")

# Q5----------------------------------
# num = int(input("enter a number: "))
# if num >= 10 and num <= 50 :
#     print(" number is in range")

# else:
#     print("number is out of range")

# Q6-----------------------------------
# m = int(input("enter maths marks: "))
# e = int(input("enter english marks: "))

# if m >= 40 and e >= 40:
#     print("pass! ")

# elif m >=80 or e >= 80:
#     print("pass! ")

# else:
#     print("fail! ")

# Q7----------------------------------
# char = input("enter a character : ")

# # if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
# if char in "AEIOUaeiou":
#     print("its a vowel. ")

# else:
#     print("consonant. ")


# Q8----------------------------------
# year = int(input("enter your year: "))

# if year % 100 == 0 and year % 400 == 0:
#     print("leap year! ")

# elif year % 100 != 0 and year % 4 == 0:
#     print("leap year! ")

# else:
#     print("normal year! ")

# Q9----------------------------------
# num = int(input("enter a number: "))

# if (num % 3 == 0 and num % 5 == 0) or (num % 7 == 0 and num % 10 != 0):
#     print("special number! ")

# else:
#     print("not a special number")


