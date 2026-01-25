#VARIABLES
#1. What is a correct way to declare a Python variable? - x = 5
#2. True or False: You can declare string variables with single or double quotes. - True
#3. True or False: Variable names are not case-sensitive. - False
#4. Select the correct functions to print the data type of a variable: - print(type(myvar))

#Variable Names
#1.Which is NOT a legal variable name? - my-var = 20
#2.Create a variable named carname and assign the value Volvo to it. - carname = "Volvo"
#3.Create a variable named x and assign the value 50 to it. - x = 50

#Multiple Variable Values
#1.What is a correct syntax to add the value 'Hello World', to 3 variables in one statement? - x = y = z = 'Hello World'
#2.Insert the correct syntax to assign values to multiple variables in one line: x,y,z = "Orange", "Banana", "Cherry"
#3.Consider the following code:
'''
fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)
What will be the result of a
'''
#a = apple

#Output Variable
#1.consider the following code:print('Hello', 'World') What will be the printed result? - Hello World
#2.
'''
Consider the following code:
a = 'Hello'
b = 'World'
print(a + b)
What will be the printed result?
'''
# HelloWorld
#3.
'''
Consider the following code:
a = 4
b = 5
print(a + b)
What will be the printed result?
'''

#Global Variables
#1.
'''
Consider the following code:
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
What will be the printed result?
'''
# Python is awesome
#2.
'''
Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
    x
  x = "fantastic"
'''
#global
#3.
'''
Consider the following code:
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
What will be the printed result?
'''
#Python is fantastic