#STRING SLICING
b = "Hello, World!"
print(b[2:5])
#examples
print(b[1:])
print(b[2:3])
print(b[:])
print(b[0:3])
#slicing from start
b = "Hello, World!"
print(b[:5])
#examples
print(b[:5])
print(b[:3])
print(b[:2])
#to end
b = "Hello, World!"
print(b[2:])
#examples
print(b[1:])
print(b[0:])

#Negative indexing
b = "Hello, World!"
print(b[-5:-2])
#examples
print(b[0:-2])
print(b[-2:-1])
print(b[:-1])

#MODIFICATON
#upper case
a = "Hello, World!"
print(a.upper())
#lower case
a = "Hello, World!"
print(a.lower())

#remove backspace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replacing string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#examples
print(a.split(" ")) # returns ['Hello,' ' World!']
print(a.split("!")) # returns ['Hello, World']

#CONCATENATION
a = "Hello"
b = "World"
c = a + b
print(c)
#examples
c = a+b
print(a+a)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#STRING FORMAT
#f srings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#examples
price = 59
txt = f"The price is {price} dollars"
print(txt)
print(f"The price is {input()} dollars")

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#ESCAPE CHARACTERS

#\'	Single Quote
#\\	Backslash
#\n	New Line
#\r	Carriage Return
#\t	Tab
#\b	Backspace
#\f	Form Feed
#\ooo	Octal value
#\xhh	Hex value

#STRING METHODS
a = "Hello, World!"
#examples
print(a.capitalize())
print(a.casefold())
print(a.center(a[1]))
print(a.count("a"))
print(a.encode())
print(a.endswith("a"))
print(a.expandtabs())
print(a.find("a"))
print(a.format())
print(a.isdigit(a[1]))

#OTHER METHODS
'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''