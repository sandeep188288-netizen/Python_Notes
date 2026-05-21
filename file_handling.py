# file = open('loops.py')
# print(file.read())


"""
MODES
---------
w - write mode(1.agar file created nahi hai to create ho jaegi 2. aur agar purana data hai to overwrite ho jaega)
a - append mode
r - raed mode
x - create mode
---------

"""
# file = open('thor.txt', 'w')
# file.write('this is thor file.')
# file.close()

# file = open('thor.txt', 'a')
# file.write('the content is added using a (append) mode ')
# file.close()

# file = open('thor.txt', 'r')
# for i in file:
    # print(i)


# with satement(auto close)
'''
with open('thor.txt','r') as file:
    print(file.read())

with open('thor.txt','w') as file:
    file.write('content overwritten')
    print('DONE')

'''

# paths


from pathlib import Path
p = Path('thor.txt')
if p.exists():
    print('file exist')
else:
    print('file not exist')