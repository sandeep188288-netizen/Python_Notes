# d = {"one":1, "two":2
# print(d[three])

# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50, 6:60}


# for i in d1:
#     print(i)
#     print(d1[i])

# d1 = {1:10, 2:20, 3:30}

# d1[4] = 40           #insertion
# print(d1)

# del d1[1]             #deletion
# print(d1)


# METHOD
# d1 = {1:10, 2:20, 3:30}

# print(d1.get(3))
# print(d1[3])   #or

# print(d1.keys())
# print(d1.pop(3))
# print(d1)

# d1.setdefault(4,40)
# print(d1)

# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50, 6:60}

# d1.update(d2)
# print(d1)

# print(d2.values())

# ------------------------------------------------------

# d1 = {1:10, 2:20, 3:30}
# d2 = {4:40, 5:50, 6:60}


# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# ------------------------------------------------------

# d1 = {1:10, 2:20, 3:30}
# d2 = {3:40, 5:50, 6:60}


# for i in d2:               # access the keys only inside a for loop 
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]

#     else:
#         d1[i] = d2[i]

# print(d1)

# ------------------------------------------------------

# l = [1,1,1,2,2,2,2,3,4,5,5,5,7,8,9,9]

# d = {}
# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(f"frrequency of an elements are : {d}" )


# ------------------------------------------------------

# a = {1:10, 2:20, 3:30}
# b = {3:40, 5:50, 6:60}

# for i in b:
#     if i in a.keys():
#         a[i] = a[i] + b[i]

#     else:
#         a[i] = b[i]

# print(a)

# ------------------------------------------------------

l = [3,2,3,2,2,2]
                        #count occurence of element (3:2, 2:4)

#------ LC 2206-------
'''
d = {}  
for i in l:
    if i in d:
        d[i] += 1

    else:
        d[i] = 1

for i in d.values():
    if i % 2 != 0:
        print("pair")
else:
        print("non pair")'''

#---------- LC 2341 ---------
'''
d = {}
for i in l:
    if i in d:
        d[i] += 1

    else:
        d[i] = 1

pairs = 0
leftovers = 0

for i in d.values():
    pairs += i//2
    leftovers += i%2

return [pairs, leftovers]  '''

# -----------(LC 2357)---------------

