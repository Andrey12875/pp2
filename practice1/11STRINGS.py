#strings

print("Hello")
print('Hello')

#quotes in quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#examples
print("'")
print("'hello'")
print('"help"')

#variables
a = "Hello"
#examples
b = "Johnny"
c = "o for"

#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
#example
v = '''
e
x
a
m
p
l
e
'''

#STRINGS ARE ARRAYS
a = "Hello, World!"
print(a[1],a[0],a[2])

for x in "banana":
  print(x)

#str length
a = "Hello, World!"
print(len(a))
#example
b = "hello"
print(len(b))

#str check
txt = "The best things in life are free!"
print("free" in txt)
#examples
print("best" in txt)
print("life" in txt)
print("the" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#check if not
txt = "The best things in life are free!"
print("expensive" not in txt)
#examples
print("best" not in txt)
print("asd" not in txt)
print("them" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#EXERCISES
#1.What will be the result of the following code:x = 'Welcome' print(x[3]) - 'c'
#2.Use the len function to print the length of the string. x = "Hello World" print(  ) - len(x)
#3.Get the first character of the string txt. txt = "Hello World" x = txt[0]

