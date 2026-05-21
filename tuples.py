"""
1. tuples are ordered(indexing)
2. can have duplicacy
3. are hetrogeneous
4. are immutable
"""

# t = ()      #empty tuple
# t = (1,2,3,4,5)

# direct loop
# # for i in t:
# #     print(i)

#indirect loop
# for i in range(len(t)):
#     print(i, t[i])

# OR

# for index, values in enumerate(t):   #********(except dict and set)
#     print(index, values)

#--------------------------------------------

# t = (1,2,3,4,5)
# print(t[1:4])       #slicing

#--------------------------------------------
#. occurence of any value

# t = (1,2,2,2,2,3,4,5,5,5,6)

# print(t.count(2))
# print(t.index(2))         #gives the first occurence only

#--------------------------------------------

# MEMBERSHIP OPERATOR

# t = (1,2,2,2,3,3,4,5,6,6,6)
# print(3 in t)
# print (9 in t)


#--------------------------------------------
#tuple unpacking

# t = (1,2,3,4,5)
# a,b,c,d,e = t           # unpacking
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


# a = 1,2                 # packing

#--------------------------------------------

# star expresion (*)

# t = (1,2,3,4,5)
# a,*b,c = t
# print(a)
# print(b)        # middle value extraction
# print(c)

# a,*b,c = (1,2,3,4,5)
# print(a)
# print(c)

