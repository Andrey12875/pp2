# Python Operators
# Operators are used to perform operations on variables and values.
# Python divides the operators into groups: arithmetic, assignment, comparison,
# logical, identity, membership, and bitwise operators.


# Arithmetic Operators
x = 10
y = 5

print(x + y)    # addition
print(x - y)    # subtraction
print(x * y)    # multiplication
print(x / y)    # division
print(x % y)    # modulus
print(x ** y)   # exponent
print(x // y)   # floor division

#example
print(3 + 2)
print(8 - 4)
print(7 * 5)
print(9 / 3)
print(2 ** 3)


# Assignment Operators
a = 5
a += 3    # same as a = a + 3
print(a)

a *= 2    # same as a = a * 2
print(a)

a -= 1    # same as a = a - 1
print(a)
#example
b = 10
b -= 2
print(b)
b /= 4
print(b)
b %= 3
print(b)
b **= 2
print(b)
b //= 2
print(b)


# Comparison Operators
print(x == y)   # equal
print(x != y)   # not equal
print(x > y)    # greater than
print(x < y)    # less than
print(x >= y)   # greater or equal
print(x <= y)   # less or equal

#example
print(4 == 4)
print(5 != 2)
print(10 > 7)
print(6 < 2)
print(3 <= 3)


# Logical Operators
print(True and False)   # returns True if both true
print(True or False)    # returns True if at least one is true
print(not True)         # reverses True to False

#example
print(5 > 2 and 2 < 10)
print(3 > 5 or 4 == 4)
print(not False)
print(1 < 0 and 2 < 3)
print(7 > 3 or 1 > 8)


# Identity Operators
x = ["apple", "banana"]
y = x

print(x is y)         # True if same object
print(x is not y)     # False if same object

#example
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a is not b)
c = a
print(c is a)
print(c is not a)
print([] is [])


# Membership Operators
fruit = ["apple", "banana", "cherry"]
print("banana" in fruit)      # True if found
print("pear" not in fruit)    # True if not found

#example
nums = [1, 2, 3]
print(1 in nums)
print(4 in nums)
print("a" not in "cat")
print("b" in "dog")
print(10 not in [5,6,7])


# Bitwise Operators
a = 6  # binary 0110
b = 3  # binary 0011

print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR
print(~a)      # NOT
print(a << 1)  # shift left
print(b >> 1)  # shift right

#example
print(4 & 1)
print(5 | 2)
print(6 ^ 3)
print(~5)
print(1 << 2)