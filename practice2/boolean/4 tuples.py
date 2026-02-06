# Python Tuples
# Tuples are used to store multiple items in a single variable.
# Tuples are ordered, unchangeable, and allow duplicate values.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#example
a = (1, 2, 3)
print(a)

b = ("x", "y", "x")
print(b)

c = ()
print(c)

d = (True, False, True)
print(d)

e = (1, "apple", 3.14)
print(e)
# Access Tuples
# You can access tuple items by index.

thistuple = ("apple", "banana", "cherry")
print(thistuple[0])
print(thistuple[-1])

#example
a = (10, 20, 30)
print(a[1])

b = ("a", "b", "c", "d")
print(b[2])

c = (1,)
print(c[0])

d = (5, 6, 7)
print(d[-2])

e = ("x", "y")
print(e[1])
# Update Tuples
# Tuples are unchangeable, but you can convert them to a list to update them.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "orange"
thistuple = tuple(y)
print(thistuple)

#example
a = (1, 2, 3)
b = list(a)
b[0] = 10
a = tuple(b)
print(a)

c = ("x", "y")
d = list(c)
d.append("z")
c = tuple(d)
print(c)

e = (True, False)
f = list(e)
f[1] = True
e = tuple(f)
print(e)

g = (0,)
h = list(g)
h[0] = 5
g = tuple(h)
print(g)
# Unpack Tuples
# You can unpack tuple values into variables.

fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits
print(a)
print(b)
print(c)

#example
x = (1, 2)
(a, b) = x
print(a, b)

y = (10, 20, 30)
(i, j, k) = y
print(i, j, k)

z = ("a", "b", "c")
p, q, r = z
print(p)

t = (True, False)
m, n = t
print(n)

u = (5, 6, 7)
x, y, z = u
print(x + y + z)
# Loop Tuples
# You can loop through tuples using for or while loops.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#example
for i in (1, 2, 3):
    print(i)

a = ("x", "y")
i = 0
while i < len(a):
    print(a[i])
    i += 1

for c in ("a",):
    print(c)

for _ in (0, 0):
    print("hi")

for x in ():
    print(x)
# Join Tuples
# You can join tuples using the + operator or by repeating them.

tuple1 = ("a", "b")
tuple2 = (1, 2)
tuple3 = tuple1 + tuple2
print(tuple3)

#example
a = (1, 2)
b = (3, 4)
print(a + b)

c = ("x",)
print(c * 3)

d = (True, False)
print(d + d)

e = ()
print(e + (1,))

f = ("a", "b")
print(f * 2)
# Tuple Methods
# Python has two built-in tuple methods: count() and index().

thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple.count("apple"))
print(thistuple.index("banana"))

#example
a = (1, 2, 2, 3)
print(a.count(2))

b = ("x", "y", "z")
print(b.index("y"))

c = (True, False, True)
print(c.count(True))

d = (5, 6, 7)
print(d.index(7))

e = ("a", "b", "a", "a")
print(e.count("a"))
# Tuple Exercises
# Example exercises with tuples.

#example
a = (1, 2, 3)
print(len(a))

b = (5,)
print(type(b))

c = ("x", "y", "z")
print("x" in c)

d = (1, 2, 3)
e = d + (4,)
print(e)

f = (10, 20)
x, y = f
print(x * y)
