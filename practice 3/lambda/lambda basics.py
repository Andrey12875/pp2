square = lambda number: number ** 2
print(square(5))

cube = lambda number: number ** 3
print(cube(3))

add = lambda first, second: first + second
print(add(7, 4))

multiply = lambda first, second: first * second
print(multiply(6, 8))

bigger = lambda first, second: first if first > second else second
print(bigger(12, 9))

smaller = lambda first, second: first if first < second else second
print(smaller(12, 9))

length = lambda text: len(text)
print(length("asdfgh"))

reverse = lambda text: text[::-1]
print(reverse("qwert"))

check = lambda number: number % 2 == 0
print(check(10))

profile = lambda name, age: {"name": name, "age": age}
print(profile("zxcv", 18))