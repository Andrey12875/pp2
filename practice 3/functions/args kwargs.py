def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def multiply(*numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


def words(*items):
    for item in items:
        print(item)


def profile(**data):
    return data


def show(**data):
    for key, value in data.items():
        print(key, value)


def names(*items):
    result = []

    for item in items:
        result.append(item)

    return result


def settings(**options):
    if options["active"]:
        return "asdf"
    else:
        return "qwer"


def combine(*numbers, **data):
    total = sum(numbers)

    result = {
        "total": total,
        "data": data
    }

    return result


def filtereven(*numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


def create(*items, **data):
    result = {
        "items": items,
        "data": data
    }

    return result


total = add(3, 5, 7, 9)
print(total)

product = multiply(2, 3, 4)
print(product)

words("asdf", "qwer", "zxcv")

person = profile(name="hjkl", age=18, active=True)
print(person)

show(name="tyui", city="bnmv", age=20)

result = names("asdf", "ghjk", "cvbn")
print(result)

status = settings(active=True)
print(status)

data = combine(5, 10, 15, name="qwer", active=False)
print(data)

nums = filtereven(1, 2, 3, 4, 5, 6)
print(nums)

final = create("asdf", "zxcv", name="hjkl", level=3)
print(final)