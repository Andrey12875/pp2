numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda number: number % 2 == 0, numbers))
print(result)

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda number: number % 2 != 0, numbers))
print(result)

numbers = [4, 12, 7, 18, 3]
result = list(filter(lambda number: number > 10, numbers))
print(result)

numbers = [4, 12, 7, 18, 3]
result = list(filter(lambda number: number < 10, numbers))
print(result)

words = ["asdf", "q", "zxcv", "hj"]
result = list(filter(lambda word: len(word) > 2, words))
print(result)

words = ["asdf", "qwer", "zxcv", "hjkl"]
result = list(filter(lambda word: word.startswith("q"), words))
print(result)

words = ["asdf", "qwer", "zxcv", "hjkl"]
result = list(filter(lambda word: "a" in word, words))
print(result)

users = [
    {"name": "asdf", "active": True},
    {"name": "qwer", "active": False},
    {"name": "zxcv", "active": True}
]
result = list(filter(lambda user: user["active"], users))
print(result)

users = [
    {"name": "hjkl", "age": 17},
    {"name": "tyui", "age": 21},
    {"name": "bnmv", "age": 15}
]
result = list(filter(lambda user: user["age"] >= 18, users))
print(result)

numbers = [0, 1, 2, 0, 3, 0, 4]
result = list(filter(lambda number: number != 0, numbers))
print(result)