# Logical Operators
# Logical operators are used to combine conditional statements.

a = 200
b = 33
c = 500
if a > b and c > a:
    print("both conditions are True")

#example
x = 10
if x > 5 and x < 20:
    print("between")

y = 0
if y == 0 or y == 1:
    print("zero or one")

flag = False
if not flag:
    print("not true")

n = 5
if n > 0 and n % 5 == 0:
    print("positive multiple of 5")

if True or False:
    print("always true")