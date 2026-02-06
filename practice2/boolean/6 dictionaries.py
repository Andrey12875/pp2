# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is ordered, changeable, and does not allow duplicates.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#example
a = {"x": 1, "y": 2}
print(a)

b = {1: "one", 2: "two"}
print(b)

c = {}
print(c)

d = {"a": 1, "a": 2}
print(d)

e = {"bool": True, "num": 10}
print(e)
# Access Items
# You can access dictionary items by referring to its key.

print(thisdict["brand"])
print(thisdict.get("model"))

#example
a = {"x": 10, "y": 20}
print(a["x"])

b = {"a": 1}
print(b.get("a"))

c = {"k": "v"}
print(c.get("missing"))

d = {1: "one"}
print(d[1])

e = {"x": None}
print(e["x"])
# Change Items
# You can change the value of a specific item by referring to its key.

thisdict["year"] = 2020
print(thisdict)

#example
a = {"x": 1}
a["x"] = 100
print(a)

b = {"a": 1, "b": 2}
b["b"] = 0
print(b)

c = {"k": True}
c["k"] = False
print(c)

d = {"x": 1}
d.update({"x": 2})
print(d)

e = {"a": 1}
e.update({"b": 2})
print(e)
# Add Items
# Adding an item to the dictionary is done by using a new index key.

thisdict["color"] = "red"
print(thisdict)

#example
a = {}
a["x"] = 1
print(a)

b = {"a": 1}
b["b"] = 2
print(b)

c = {"x": 0}
c.update({"y": 1})
print(c)

d = {}
d.update({1: "one"})
print(d)

e = {"a": 1}
e["a"] = 99
print(e)
# Remove Items
# You can remove items using pop(), del, popitem(), or clear().

thisdict.pop("model")
print(thisdict)

#example
a = {"x": 1, "y": 2}
a.pop("x")
print(a)

b = {"a": 1}
del b["a"]
print(b)

c = {"x": 1, "y": 2}
c.popitem()
print(c)

d = {"k": 1}
d.clear()
print(d)

e = {"x": 1}
del e
# Loop Dictionaries
# You can loop through a dictionary by keys, values, or items.

for x in thisdict:
    print(x)

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)

#example
a = {"x": 1, "y": 2}
for k in a:
    print(k)

for v in a.values():
    print(v)

for k, v in a.items():
    print(k, v)

for _ in {}:
    print(_)

for k in {"a": 1}:
    print(k)
# Copy Dictionaries
# You cannot copy a dictionary simply by assignment.

thisdict = {"a": 1, "b": 2}
mydict = thisdict.copy()
print(mydict)

#example
a = {"x": 1}
b = a.copy()
print(b)

c = dict(a)
print(c)

d = a
d["x"] = 5
print(a)

e = {"k": 0}
f = e.copy()
f["k"] = 10
print(e)
# Nested Dictionaries
# A dictionary can contain dictionaries.

myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007}
}
print(myfamily)

#example
a = {
    "x": {"v": 1},
    "y": {"v": 2}
}
print(a)

b = {"a": {"b": {"c": 1}}}
print(b)

c = {"n": {}}
print(c)

d = {"x": {"y": 0}}
print(d["x"]["y"])

e = {
    1: {"value": True},
    2: {"value": False}
}
print(e)
# Dictionary Methods
# Python has many built-in dictionary methods.

thisdict = {"a": 1, "b": 2}
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

#example
a = {"x": 1}
print(a.keys())

b = {"x": 1}
print(b.values())

c = {"x": 1}
print(c.items())

d = {"a": 1}
print(d.get("a"))

e = {"x": 1}
print("x" in e)