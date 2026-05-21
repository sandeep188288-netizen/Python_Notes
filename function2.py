'''
problem -> humme nahi pta kitne parametres pass honge function me -> so use args -> *args
args -> notation -> *a
variable_name -> a (koi bhi name de sakte hai)
args values ko accept karte in the form "tuple"


'''

def add(*numbers):
    for i in numbers:
        print(i)
add(1,2,3,4,5)

def polio(name, age, pin, contact):
    print(name,age,pin,contact)
polio(name = "raju", age = 12, pin = 123456, contact = 1234567890)

'''
kwargs -> keyword arguments -> **kwargs
denote -> **var_name -> var_name (koi bhi name de sakte hai)
kwargs values ko accept karte in the form "dictionary"

'''
def polio(**variable):
    # print(variable)
    for i in variable:
        print(i,"=", variable[i])       # parameter = keys & arguments = values
polio(name = "raju", age = 12, pin = 123456, contact = 1234567890)


"""
lambda function -> function in a single line
lambda = keyword
a,b:a+b -> agar a and b varibale me koi value aaegi to hi a+b chlehaga
"""

add = lambda a,b : a+b
print(add(10,20))

