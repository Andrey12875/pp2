# Python Lists
# Lists are used to store multiple items in a single variable.
# Lists are ordered, changeable, and allow duplicate values.

# Creating a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#example
a = [1, 2, 3]
b = ["cat", "dog", "cat"]
c = []
d = [True, False, True]
e = [1, "apple", 3.5]


# List length
print(len(thislist))

#example
print(len([1, 2, 3, 4]))
print(len([]))
print(len(["a"]))
print(len(["x", "y", "z"]))
print(len([0, 0, 0]))


# List items have data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#example
print([1.1, 2.2, 3.3])
print(["one", 2, False])
print([[], [], []])
print([None, None])
print([0, "0", False])


# Access list items by index
print(thislist[0])
print(thislist[1])
print(thislist[2])

#example
nums = [10, 20, 30, 40]
print(nums[0])
print(nums[3])
print(nums[-1])
print(nums[-2])
print(nums[1])


# Change list items
thislist[1] = "blackcurrant"
print(thislist)

#example
x = [1, 2, 3]
x[0] = 100
print(x)
x[2] = 0
print(x)
x[1] = -5
print(x)
x[0] = x[1]
print(x)


# Loop through a list
for item in thislist:
    print(item)

#example
for i in [1, 2, 3]:
    print(i)
for c in ["a", "b", "c"]:
    print(c)
for v in []:
    print(v)
for x in [True, False]:
    print(x)
for n in [10]:
    print(n)


# Check if item exists
print("apple" in thislist)
print("orange" in thislist)

#example
print(1 in [1, 2, 3])
print("a" in ["a", "b"])
print("x" not in ["x", "y"])
print(5 in [])
print(False in [False, True])


# Add items
thislist.append("orange")
print(thislist)

#example
a = []
a.append(1)
print(a)
a.append(2)
print(a)
a.append("x")
print(a)
a.append(True)
print(a)
a.append(None)
print(a)


# Remove items
thislist.remove("banana")
print(thislist)

#example
x = [1, 2, 3, 4]
x.remove(2)
print(x)
x.remove(4)
print(x)
y = ["a", "b", "c"]
y.remove("a")
print(y)
z = [True, False]
z.remove(False)
print(z)


# List constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

#example
print(list((1, 2, 3)))
print(list("abc"))
print(list(range(3)))
print(list((True, False)))
print(list([]))

# Change List Items
# You can change list items by referring to their index.

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#example
a = [1, 2, 3]
a[0] = 10
print(a)

b = ["x", "y", "z"]
b[2] = "w"
print(b)

c = [True, False]
c[1] = True
print(c)

d = [0, 0, 0]
d[2] = 5
print(d)

e = ["a"]
e[0] = "b"
print(e)

# Add List Items
# You can add items using append(), insert(), or extend().

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#example
a = []
a.append(1)
print(a)

b = [1, 2]
b.insert(1, 100)
print(b)

c = [1]
c.extend([2, 3])
print(c)

d = ["a"]
d.append("b")
print(d)

e = [0]
e.extend([1, 2, 3])
print(e)

# List Comprehension
# List comprehension offers a shorter syntax for creating new lists.

fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#example
a = [x for x in range(5)]
print(a)

b = [x for x in range(10) if x % 2 == 0]
print(b)

c = [x.upper() for x in ["a", "b", "c"]]
print(c)

d = [x*x for x in [1, 2, 3]]
print(d)

e = [x for x in "hello"]
print(e)

# Sort Lists
# Lists can be sorted using sort().

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#example
a = [3, 1, 2]
a.sort()
print(a)

b = [5, 2, 9]
b.sort(reverse=True)
print(b)

c = ["b", "a", "c"]
c.sort()
print(c)

d = [10, 1, 100]
d.sort()
print(d)

e = [True, False]
e.sort()
print(e)

# Copy Lists
# You cannot copy a list simply by assignment.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#example
a = [1, 2, 3]
b = a.copy()
print(b)

c = list(a)
print(c)

d = a[:]
print(d)

e = []
e = a.copy()
print(e)

f = a
f.append(4)
print(a)

# Join Lists
# You can join lists using +, extend(), or loops.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#example
a = [1, 2]
b = [3, 4]
print(a + b)

c = [1]
c.extend([2, 3])
print(c)

d = []
for x in [5, 6]:
    d.append(x)
print(d)

e = ["x"]
e += ["y", "z"]
print(e)

f = []
f.extend([])
print(f)
# List Methods
# Python has built-in list methods.

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
thislist.remove("banana")
print(thislist)

#example
a = [1, 2, 3]
a.insert(1, 100)
print(a)

b = [1, 2, 3]
b.pop()
print(b)

c = [1, 2, 2, 3]
print(c.count(2))

d = [3, 1, 2]
d.sort()
print(d)

e = [1, 2, 3]
e.reverse()
print(e)