# Q------------------------------------------

# n = int(input("enter a no. : "))
# count = 0
# while n > 0:
#     # digit = n%10
#     count += 1
#     n = n//10
# print(count)

# Q------------------------------------------

# def count(n):
#     n = 1234
#     count = 0
#     while n > 0:
#         count += 1
#         n = n//10
#     print(count)
# count(123)

# Q------------------------------------------
#  ********* IF WE USE A RETURN STATEMENT INSIDE A FUNCTION 
# IT WILL ACT LIKE A MINI VARIABLE THEN WE HAVE TO PRINT IT *************


# def count(n):
#     n = 1234
#     count = 0
#     while n > 0:
#         count += 1
#         n = n//10
#     return(count)
# print(count(123))

# Q------------------------------------------

# n = 123
# sum = 0
# while n > 0:
#     digit = n%10
#     sum = sum+digit
#     n = n//10
# print(sum)

'''def check_sum(n:int):  # n:int => PARAMETER ANNOTATION
    sum = 0
    while n > 0:
        digit = n%10
        sum = sum+digit
        n = n//10
    return(sum)

print(check_sum(1234567))'''

# Q------------------------------------------(armstrong number)

n = 153
copy = n
sum = 0
while n>0:
    digit = n%10
    pow = digit ** len(str(n))
    sum += pow
    n = n//10

if sum == copy:
    print("Armstrong number! ")
else:
    print("not an Armstrong number! ")