numbers = [5, 2, 9, 1, 7]
result = sorted(numbers, key=lambda number: number)
print(result)

numbers = [5, 2, 9, 1, 7]
result = sorted(numbers, key=lambda number: number, reverse=True)
print(result)

words = ["asdf", "q", "zxcv", "hj"]
result = sorted(words, key=lambda word: len(word))
print(result)

words = ["asdf", "qwer", "zxcv", "hjkl"]
result = sorted(words, key=lambda word: word[-1])
print(result)

users = [
    {"name": "asdf", "age": 17},
    {"name": "qwer", "age": 20},
    {"name": "zxcv", "age": 15}
]
result = sorted(users, key=lambda user: user["age"])
print(result)

users = [
    {"name": "hjkl", "age": 18},
    {"name": "tyui", "age": 22},
    {"name": "bnmv", "age": 16}
]
result = sorted(users, key=lambda user: user["name"])
print(result)

points = [(3, 7), (1, 9), (5, 2)]
result = sorted(points, key=lambda point: point[0])
print(result)

points = [(3, 7), (1, 9), (5, 2)]
result = sorted(points, key=lambda point: point[1])
print(result)

data = [
    {"name": "asdf", "score": 80},
    {"name": "qwer", "score": 95},
    {"name": "zxcv", "score": 70}
]
result = sorted(data, key=lambda item: item["score"], reverse=True)
print(result)

words = ["asdf", "qwer", "zxcv", "hjkl"]
result = sorted(words, key=lambda word: word[1])
print(result)