# The pass Statement
# The pass statement is used as a placeholder for future code.
# It allows you to avoid errors when an empty statement is required.

a = 33
b = 200

if b > a:
    pass

#example
x = 10
if x > 0:
    pass

y = -5
if y < 0:
    pass
else:
    print("non-negative")

flag = True
if flag:
    pass
print("program continues")

if False:
    pass
print("after empty if")