# Nested If
# You can have if statements inside if statements.

x = 41
if x > 10:
    print("above ten")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20")

#example
a = 5
if a > 0:
    if a < 10:
        print("between 0 and 10")

n = -3
if n <= 0:
    if n < 0:
        print("negative")

age = 20
if age >= 18:
    if age >= 21:
        print("21+")
    else:
        print("adult but <21")

x = 0
if x == 0:
    if True:
        print("zero confirmed")

flag = True
if flag:
    if flag:
        print("nested true")