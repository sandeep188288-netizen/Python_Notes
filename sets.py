'''1. Unordered (no indexing)
2. semi-Mutable(can add butt cannot change or remove)
3. Unique elements(no duplicates)
4. Hetrogeneous(can contain different data types)'''

# Creating a set
# a = []
# b = {}

# c = set()        #type conversion

# s = set()       # empty set

# s = {1,2,3,4,5,6,7,8}
# print(s)

'''
* METHODS IN SET

1. add()
2. update()
3. remove()
4. discard()
5. pop()
6. clear()
'''
#Add
# s= {1,2,3,4,5}
# s.add(6)

#update
# s.update([6,7,8])
# print(s)

# # remove().  # if value not present then we get an error
# s.remove(1)
# # print(s)


# # Discard()   #if value not present and does'nt get an error as output
# s.discard(10)
# print(s)

# #pop()
# s = {4,3,2,6,7,8}
# print(s.pop())  #removes first smallest element from the first


#clear(). #removes all the elements and gives an empty set
# s = {1,2,3,4,5}
# s.clear()
# print(s)

'''
1. Intersection
2. Union
3. Difference
4. Symmetric Difference

'''


# s1 = {1,2,3,4}
# s2 = {2,3,4,6}

# # 1. INTERSECTION. => same elements
# print(s1.intersection(s2))


# # 2. UNION
# print(s1.union(s2))

# #3. DIFFERENCE.  =>  elements in first set and not in second set
# print(s1.difference(s2))
# print(s2.difference(s1))

# # 4. SYMMETRUC DIFFERENCE
# print(s1.symmetric_difference(s2))

#  frozen set
fs = {10,20,30,40,50}
fs = frozenset(fs)               # frozenset is a functon
fs.remove(10)
print(fs)
