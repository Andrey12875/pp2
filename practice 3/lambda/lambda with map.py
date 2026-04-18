numbers = [1, 2, 3, 4, 5]
result = list(map(lambda number: number * 2, numbers))
print(result)

numbers = [2, 4, 6, 8]
result = list(map(lambda number: number + 10, numbers))
print(result)

numbers = [3, 5, 7, 9]
result = list(map(lambda number: number ** 2, numbers))
print(result)

words = ["asdf", "qwer", "zxcv"]
result = list(map(lambda word: len(word), words))
print(result)

words = ["asdf", "qwer", "zxcv"]
result = list(map(lambda word: word[::-1], words))
print(result)

numbers = [10, 20, 30]
result = list(map(lambda number: number / 2, numbers))
print(result)

users = [
    {"name": "asdf", "age": 17},
    {"name": "qwer", "age": 20},
    {"name": "zxcv", "age": 15}
]
result = list(map(lambda user: user["name"], users))
print(result)

users = [
    {"name": "hjkl", "age": 18},
    {"name": "tyui", "age": 22},
    {"name": "bnmv", "age": 16}
]
result = list(map(lambda user: user["age"], users))
print(result)

numbers = [1, 2, 3, 4]
result = list(map(lambda number: number % 2 == 0, numbers))
print(result)

first = [1, 2, 3]
second = [10, 20, 30]
result = list(map(lambda a, b: a + b, first, second))
print(result)