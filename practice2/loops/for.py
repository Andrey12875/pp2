"""
For loops

A for loop is used to iterate over a sequence (like list, string, tuple, etc.).
It runs the block of code once for each item in the sequence.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#example
for i in [1, 2, 3]:
    print(i)

for c in "abc":
    print(c)

for b in (10, 20, 30):
    print(b)

for v in {True, False}:
    print(v)

for n in range(3):
    print("num", n)

"""
Looping through a string

A string is a sequence, so a for loop can iterate its characters.
"""

for x in "banana":
    print(x)

#example
for c in "hello":
    print(c)

for c in "123":
    print(c)

for c in "-_-":
    print(c)

for c in "":
    print("nothing")

for c in "Py":
    print(c)
"""
The break statement

break stops the loop even if there are still items left.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#example
for i in [1, 2, 3, 4]:
    if i == 3:
        break
    print(i)

for c in ["a", "b", "c"]:
    if c == "b":
        break
    print(c)

for n in range(5):
    if n == 4:
        break
    print(n)

names = ["Tom", "Sam", "Joe"]
for name in names:
    if name == "Sam":
        break
    print(name)

for i in (10, 20, 30):
    if i == 20:
        break
    print(i)
"""
The continue statement

continue stops the current iteration and moves to the next.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#example
for i in [1, 2, 3, 4]:
    if i == 2:
        continue
    print(i)

for c in "hello":
    if c == "l":
        continue
    print(c)

for n in range(5):
    if n % 2 == 1:
        continue
    print(n)

for b in (True, False, True):
    if not b:
        continue
    print(b)
"""
The else statement

Else with a for loop runs once after the loop finishes normally.
If the loop is stopped by break, else will NOT run.
"""

for x in range(4):
    print(x)
else:
    print("done")

#example
for i in [1, 2]:
    print(i)
else:
    print("finished")

for c in ["a"]:
    print(c)
else:
    print("done")

for n in []:
    print(n)
else:
    print("empty list")

for n in [1, 2, 3]:
    if n == 2:
        break
    print(n)
else:
    print("won't run")
"""
Looping through different sequences

You can use for loops on lists, tuples, sets, strings, ranges.
"""

# list example
for x in ["a", "b", "c"]:
    print(x)

# tuple example
for x in (1, 2, 3):
    print(x)

# set example
for x in {1, 2, 3}:
    print(x)

# range example
for x in range(3, 6):
    print(x)

# string example
for x in "Py":
    print(x)

#example
for i in range(5):
    print(i)

for c in ["x", "y"]:
    print(c)

for f in (True, False):
    print(f)

for s in {"apple", "banana"}:
    print(s)

for t in (10, 20, 30):
    print(t)
"""
Using range()

range(start, stop, step) generates a sequence of numbers.
"""

for i in range(6):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(2, 10, 2):
    print(i)

#example
for i in range(3):
    print(i)

for i in range(1, 4):
    print(i * 2)

for i in range(0, 10, 3):
    print(i)

for i in range(5, 0, -1):
    print(i)

for i in range(10, 15):
    print(i)
