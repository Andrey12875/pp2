# Python Sets
# Sets are used to store multiple items in a single variable.
# A set is unordered, unchangeable*, and unindexed.
# *Set items are unchangeable, but you can remove and add items.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#example
a = {1, 2, 3}
print(a)

b = {"x", "y", "x"}
print(b)

c = set()
print(c)

d = {True, False, True}
print(d)

e = {1, "apple", 3.14}
print(e)
# Access Set Items
# You cannot access items by index, but you can loop through a set
# or check if an item exists.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("banana" in thisset)

#example
a = {1, 2, 3}
for i in a:
    print(i)

print(2 in a)
print(5 in a)

b = {"x", "y"}
print("x" in b)

print("z" not in b)
# Add Set Items
# You can add items using add() or update().

thisset = {"apple", "banana"}
thisset.add("cherry")
print(thisset)

#example
a = {1, 2}
a.add(3)
print(a)

b = {"x"}
b.update({"y", "z"})
print(b)

c = set()
c.add(10)
print(c)

d = {1}
d.update([2, 3, 4])
print(d)

e = {"a", "b"}
e.add("c")
print(e)
# Remove Set Items
# You can remove items using remove(), discard(), pop(), or clear().

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#example
a = {1, 2, 3}
a.discard(2)
print(a)

b = {10, 20}
b.pop()
print(b)

c = {"x", "y"}
c.clear()
print(c)

d = {1, 2}
d.remove(1)
print(d)
# Loop Sets
# You can loop through set items using a for loop.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#example
for i in {1, 2, 3}:
    print(i)

for c in {"a", "b"}:
    print(c)

for x in set():
    print(x)

for v in {True, False}:
    print(v)

for n in {10}:
    print(n)
# Join Sets
# You can join sets using union(), update(), or operators.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#example
a = {1, 2}
b = {3, 4}
print(a | b)

c = {1, 2}
c.update({2, 3})
print(c)

d = {"x"}
e = {"y"}
print(d.union(e))

f = {1, 2}
g = {2, 3}
print(f & g)

h = {1, 2, 3}
i = {3}
print(h - i)
# Frozenset
# A frozenset is an immutable version of a set.

thisfrozenset = frozenset({"apple", "banana", "cherry"})
print(thisfrozenset)

#example
a = frozenset({1, 2, 3})
print(a)

b = frozenset()
print(b)

c = frozenset([1, 1, 2])
print(c)

d = frozenset("abc")
print(d)

e = frozenset({True, False})
print(e)
# Set Methods
# Python has many built-in set methods.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.remove("banana")
print(thisset)

#example
a = {1, 2, 3}
a.discard(2)
print(a)

b = {1, 2}
c = {2, 3}
print(b.intersection(c))

d = {1, 2}
e = {2, 3}
print(d.symmetric_difference(e))

f = {1, 2, 3}
print(f.issuperset({1, 2})) 