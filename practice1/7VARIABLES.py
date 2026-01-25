#creation
x = 5
y = "John"
print(x)
print(y)
#examples
a = 1
b = True
c = "qwerty"
d = 2.34
e = '%'
print(a,b,c,d)

#type change

a = 1
a = 2

x = 4       # x is of type int
x = "Sally" # x is now of type str

print(x,a)

#casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#examples
x = str(4)    # x will be '4'
y = int(4)    # y will be 4
z = float(4)  # z will be 4.0

#Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

#Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
a, b, c = "a", "b", "c"

#One Value to Multiple Variables
x = y = z = "Orange"
a, b, c = "123"

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

#OUTPUT VARIABLES
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#GLOBAL VARIABLES
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#EXAMPLE
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
