def show_user_data():
    user_data = {
        "asdf": "qwert",
        "zxcv": 17,
        "hjkl": True
    }
    print(user_data)


def count_numbers():
    numbers = [4, 8, 2, 9, 1]
    total = sum(numbers)
    print(total)


def find_biggest_number():
    numbers = [12, 45, 7, 23, 89]
    biggest_number = max(numbers)
    print(biggest_number)


def show_items():
    items = ["asdf", "qwer", "zxcv", "tyui"]
    for item in items:
        print(item)


def check_number():
    number = 15

    if number > 10:
        print("lkjhg")
    else:
        print("mnbvc")


def create_coordinates():
    coordinates = (10, 25)
    print(coordinates)


def reverse_words():
    words = ["asdf", "qwer", "zxcv"]
    words.reverse()
    print(words)


def count_letters():
    text = "asdfghjkl"
    letters_count = len(text)
    print(letters_count)


def multiply_values():
    first_number = 6
    second_number = 7
    result = first_number * second_number
    print(result)


def show_active_users():
    users = [
        {"asdf": "qwer", "zxcv": True},
        {"asdf": "hjkl", "zxcv": False},
        {"asdf": "tyui", "zxcv": True}
    ]

    for user in users:
        if user["zxcv"]:
            print(user["asdf"])


show_user_data()
count_numbers()
find_biggest_number()
show_items()
check_number()
create_coordinates()
reverse_words()
count_letters()
multiply_values()
show_active_users()