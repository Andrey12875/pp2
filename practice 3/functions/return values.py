def getname():
    return "asdf"


def getage():
    return 19


def add(first, second):
    return first + second


def multiply(first, second):
    return first * second


def profile(name, age, active):
    data = {
        "name": name,
        "age": age,
        "active": active
    }

    return data


def evens(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


def biggest(numbers):
    result = max(numbers)
    return result


def coordinates(x, y):
    point = (x, y)
    return point


def count(text):
    result = len(text)
    return result


def active(users):
    result = []

    for user in users:
        if user["active"]:
            result.append(user["name"])

    return result


name = getname()
print(name)

age = getage()
print(age)

total = add(8, 4)
print(total)

product = multiply(6, 7)
print(product)

person = profile("qwer", 20, True)
print(person)

nums = evens([2, 5, 8, 11, 14])
print(nums)

maximum = biggest([7, 18, 3, 25, 9])
print(maximum)

point = coordinates(10, 30)
print(point)

length = count("asdfgh")
print(length)

users = [
    {"name": "zxcv", "active": True},
    {"name": "hjkl", "active": False},
    {"name": "tyui", "active": True}
]

names = active(users)
print(names)