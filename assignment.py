# Q1------------------------------------------

# n = int(input("enter a number: "))
# a = 0
# for i in range(1,n+1):
#     a = a+i

# print(a)

# Q2------------------------------------------
# n = int(input("enter a number: "))
# a = 1
# for i in range(1,n+1):
#     a = a*i

# print(a)

# Q3------------------------------------------
# n = int(input("enter a number: "))
# for i in range(2,n+1,2):
#     print(i)

# Q4------------------------------------------
# n = int(input("enter a number: "))
# for i in range(1,n+1,2):
#     print(i)

# Q5------------------------------------------
# n = int(input("enter a number: "))

# for i in range(1,n+1):
#     if i % 5 == 0:
#         print(i)
  
    
# n = int(input("enter a number: "))
# sum = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum = sum + i
        
# print(sum)
#Q--------------------------------
# n = int(input("enter a number: "))
# p = 1

# for i in range(1,n+1):
    
#         p = p * i
        
# print(p)

#Q8------------------------------------
# n = int(input("enter a number: "))

# for i in range(1,n+1):
#     print(i**2)

# Q9-----------------------------------
# n = int(input("enter a number: "))
# sum = 0

# for i in range(1,n+1):
#     if i % 2 != 0:
#         sum = sum + i
# print(sum)

# Q10-----------------------------------
# n = int(input("enter a number: "))

# for i in range(n,0,-1):
#     print(i)

# Q11-----------------------------------(not for loop)
# str1 = "P @ # y n 2 6 a t ^ & i 5 v e "
# letters = 0
# digits = 0
# symbol = 0

# for i in range(len(str1)):
#     letters += i
#     digits += i
#     symbol += i
# print ("letter: " + letters)
# print ("digits: " + letters)
# print ("symbol: " + letters)

# Q12-----------------------------------

# n = int(input("enter a number: "))

# for i in range(1,n+1):
#     print(i)

# Q13-----------------------------------
# n = int(input("enter a number: "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even += i

#     else:
#         odd += i

# print(f"evensum: {even}")
# print(f"oddsum:  {odd}")

# Q14-----------------------------------
# n = int(input("enter a number: "))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)

# Q15-------------------------------------

# n = int(input("enter a number: "))
# sum = 0
# for i in range(1,n):  # n means factor of a number except itself !!
#     if n % i == 0:
    
#         sum += i
# if sum == n:
#     print("no. is perfect")

# else:
#     print("not a perfect no.")


# Q16-------------------------------------
# n = int(input("enter a number: "))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("no. is prime number ! ")

# else:
#     print("composit number ! ")

# OR(**** optimized one ****)

# Q16-------------------------------------
# n = int(input("enter your number : "))

# for i in range(2, (n//2)+1):
#     if n%i == 0:
#         print("number is not prime! ")
#         break

# else:
#     print("number is prime! ")


# Q17-------------------------------------(odd no.)
# n = int(input("enter your number : "))

# for i in range(1,n+1):
#     if i % 2 == 0:
#         continue

#     print(i)

# Q18-------------------------------------(even no.)
# n = int(input("enter your number : "))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         # continue

#      print(i)

# Q19-------------------------------------

# a = int(input("enter a number: "))
# sum = 0
# while a != 0:  #or a > 0
#     print(a%10)
#     sum = sum + a % 10
#     a = a//10   
# print(sum)

# Q20-------------------------------------

# n = int(input("enter a number: "))
# a = n
# rev = 0
# while n != 0: 
#     # print(a%10)
#     rev = rev*10 + n % 10
#     n = n//10  
# if rev == a :
#     print("number is pallindrome")

# else:
#      print("number is not pallindrome")



#POWER SESSION:
# Q21-------------------------------------
# 1
# n = input("enter a number: ")
# print(n[::-1])
# 2(with for loop reverse)
# n = int(input("enter a number: "))
# digit = ""
# for i in str(n)[::-1]:
#     digit += i

# print(digit)
# ------------------------------------------------
# n = "hello world"
# for i in range(1,6):
#     print(n)
# print("hello world\n"*5)

# ------------------------------------------------
# q2(FIBONACCI SERIES)
# n = int(input("enter a number: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     a,b = b,a+b

# ------------------------------------------------
# q2(print the largest digit in a number)
# n = 4289
# largest = 0
# for i in str(n):
#     # if largest < int(i):
#     #     largest = int(i)
#     a = int(i)
#     if a > largest:
#         largest = a

# print(largesst)'''

# ------------------------------------------------
# q4(GUESSING GAME)
# (user guesses a number untill correct)

''' import random

riju = random.randint(1,50)

for i in range(5):
    sandeep = int(input("enter your number: "))

    if sandeep == riju:
        print("You won! ")
        break

    if sandeep < riju:
        print("Too smaller go higher! ")

    if sandeep > riju:
        print("Too higher go lower! ")

else:
    print(f"You lost! , number is {riju}" )
    '''
# ------------------------------------------------(pallindrome number)
'''n = int(input("Enter a number: "))
if str(n) == str[::-1]:
    print(f"number {n} is pallindrome number! ")

else:
    print(f"number {n} is not a pallindrome number! ")

'''
# ------------------------------------------------
# sum = 0
# while True:
#     n = int(input("Enter a number: "))

#     if n == 0:
#         break

#     sum += n

# print(sum)

# ------------------------------------------------
# n = 8934
# rev = 0
# while n!=0:
#     rev = rev*10 + n%10
#     n = n//10   

# print(rev)

# ------------------------------------------------
# ARMSTRONG NUMBER
# n = 153
# copy = n
# sum = 0
# length = len(str(n))

# while n > 0:
#     digit = n%10
#     sum += digit**length
#     n = n // 10

# if copy == sum:
#     print("Armstrong number! ")    

# else:
#     print("Not an Armstrong number! ")    

