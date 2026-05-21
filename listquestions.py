# a = int(input(" elements you want : "))
# l = []
# for i in range(a):
#     z = int(input("tell your number : "))
#     l.append(z)

# print(l)
# a = eval(input("tell your str : "))
# print(a)


# Q---------------------------------------------------------
# (reverse)
# a = [10,20,30,40,50]
# l = []
# for i in range(len(a)-1, -1, -1):
#     l.append(a[i])

# print(l)

# ***** WITH TWO PINTER

# a = [10,20,30,40,50]

# i, j = 0, len(a)-1
# while i < j:
#     a[i], a[j] = a[j], a[i]
#     i += 1
#     j -= 1
# print(a)

# **** WITH FOR LOOP

# a = [10,20,30,40,50]
# z = len(a)-1

# for i in range(len(a)//2):
#     a[i], a[z] = a[z], a[i]
#     z = z-1
# print(a)

# Q---------------------------------------------------------

# a = [10,-20,30,-40,50]
# for i in a:
#     if i >= 0:
#         print(i)
# for i in a:
#     if i < 0:
#         print(i)

# Q---------------------------------------------------------

# ************** BUBBLE SORT **********************

# a = [12,98,45,67,88,56,11]

# for j in range(len(a)-1):
#     for i in range(0,len(a)-1-j):
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
# print(a)

# Q---------------------------------------------------------

# a = [10,23,45,32,22,21,78,94,42]

# max = a[0]
# idx = 0
# for i in range(1,len(a)):
#     if a[i] > max:
#         max = a[i]
#         idx = i

# # print(max , idx)
# print(f"largest element is {max} at index {idx}")

# Q---------------------------------------------------------

# a = [10,23,45,32,22,21,90,78,94,42]

# max = a[0]
# secmax = a[0]
# m_idx = 0
# sm_idx = 0

# for i in range(1,len(a)):
#     if a[i] > max:
#         secmax = max
#         max = a[i]
#         sm_idx = m_idx
#         m_idx = i

#     elif a[i] > secmax and a[i] != max:
#         secmax = a[i]
#         sm_idx = i
     
# print(f"Second largest element is {secmax} at idx {sm_idx}")

# Q---------------------------------------------------------
# for finding smallest and sec samllets - pick greater value
#  

# a = [10,23,45,32,22,21,90,78,94,42]

# small = 1000
# secsmall = 1000
# small_idx = 0
# ssmall_idx = 0

# for i in range(1,len(a)):
#     if a[i] < small:

#         secsmall = small
#         small = a[i]
       
        
#         ssmall_idx = small_idx
#         small_idx = i

#     elif a[i] < secsmall and a[i] != small:
#         secsmall = a[i]
#         ssmall_idx = i
     
# print(f"Smallest element is {small} at idx {small_idx}")
# print(f"Second smallest element is {secsmall} at idx {ssmall_idx}")

# Q---------------------------------------------------------

# l = [1,2,8,4,5,6,7]
# for i in range(1,len(l)):
#     if l[i] < l[i-1]:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")


# Q---------------------------------------------------------
# l = [2, 3, 15,12, 3, 2]

# i = 0
# j = len(l) - 1

# while i < j:
#     if l[i] != l[j]:
#         print("Not palindrome")
#         break
#     i += 1
#     j -= 1
# else:
#     print("Palindrome")

# for i in range(len(l)//2):
#     if l[i] != l[len(l)-1-i]:
#         print("pallindrome")
#         break
# else:
#     print("mot a pallindrome")


    
# Q---------------------------------------------------------
# .split => used to do not print in string(separates al the values and digits)
# map is used to print multiple values (map accepts datatypes and inputs)
#list is for all elements inside list(covert the values in the form of data structures)

'''sabse pehle inputs accept -> har input split hoga -> input will be 
type casted in the form of int -> we stored all the int values inside a list'''

# lst = sum(list(map(int, input("enter elements : ").split()))    )
# print(lst)                                                     

# Q---------------------------------------------------------(imp)

l = [1,2,3,4,5]
k = 7
k = k%len(l)
for i in range(k):
    last = l[-1]
    for j in range(len(l)-1, 0, -1):
        l[j] = l[j-1]
    l[0] = last
print(l)


# Q---------------------------------------------------------
# assign all the zeros at the end of the list

l = [0,0,0,1,0,0,3,12]
j = 0
for i in range(len(l)):
    if l[i] != 0:
        l[i], l[j] = l[j], l[i]
        j = j+1

print(l)


 