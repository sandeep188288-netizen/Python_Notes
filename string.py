# a = "hello"

# print(a[4], a[-1])

# #string slicing 

# str = "sheryians"
# print(str[0:4:1]). => [start : stop : steps]
# print(str[0:4:2])
# print(str[0:4:3])
# print(str[::]). => [0:last word:]

# s = "hello how are you"
# print(s[6:9])
# print(s[14:17])

#UNICODE(ASCII VALUES)

# print(ord("A"))

# Q1
# a = input("give me a character : ")
# value = ord(a)

# if (value >= 65 and value <= 90) or (value >= 97 and value <= 122):
#     print("alphabets! ")

# else:
#     print("not an alphabet! ")

# Q31---------------------------------------------------******IN SLICING VALUE PRINT LENGTH-1

# s = "Shery"
# print(f"reverse is {s[::-1]} and lenght of string {len(s)}")
# print(f"string in upper format -> {s.upper()}")
# print(f"string in lower format -> {s.lower()}")

# Q32-------------------------------------------------

# s = "ShEry"
# lower = ""
# upper = ""
# for i in s:
#     if i.islower():
#         lower += i
#     else:
#         upper += i

# print(lower + upper)


# Q33-------------------------------------------------


# str1 = "P@#yn26at^&i5ve"
# alpha = 0
# digit = 0
# special = 0 
# for i in str1:
#     if i.isalpha():
#       alpha += 1
#     elif i.isdigit():
#        digit += 1

#     else:
#        special += 1

# print(f"alphabet count : {alpha}")
# print(f"digit count : {digit}")
# print(f"special count : {special}")




# def check(s):
#    str1 = "P@#yn26at^&i5ve"
#    alpha = 0
#     digit = 0
#     special = 0 
#     for i in str1:
#          if i.isalpha():
#             alpha += 1
#          elif i.isdigit():
#             digit += 1

#          else:
#             special += 1

# print(f"alphabet count : {alpha}")
# print(f"digit count : {digit}")
# print(f"special count : {special}")


# Q34-------------------------------------------------

str1 = "hello"
str2 = "hello"
if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print("strings are not same")

    else:
         print("strings are same")
else:
    print("both are unequal") 