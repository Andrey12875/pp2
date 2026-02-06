
# Python Booleans
# Booleans represent one of two values: True or False

# Comparison operators return Boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#example
print(5 > 3)
print(7 == 7)
print(2 < 1)
print(100 >= 50)
print(8 != 8)


# Booleans in if statements
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#example
x = 10
y = 20
if x < y:
    print("x is smaller")
else:
    print("x is not smaller")

n = 5
if n == 5:
    print("equal")
else:
    print("not equal")


# The bool() function evaluates any value and returns True or False
print(bool("Hello"))
print(bool(15))

#example
print(bool("Python"))
print(bool(-3))
print(bool(0))
print(bool(3.14))
print(bool(" "))


# Most values are True if they have content
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#example
print(bool([1, 2]))
print(bool({"a": 1}))
print(bool((5,)))
print(bool({1, 2, 3}))
print(bool(range(1)))


# Some values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#example
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(0.0))
print(bool(set()))



# Functions can return Boolean values
def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")

#example
def is_positive(x):
    return x > 0

print(is_positive(5))
print(is_positive(-2))

def always_false():
    return False

print(always_false())
print(is_positive(0))


# isinstance() returns True or False
x = 200
print(isinstance(x, int))

#example
print(isinstance("hello", str))
print(isinstance(3.14, float))
print(isinstance([1, 2], list))
print(isinstance((1, 2), tuple))
print(isinstance(10, bool))
