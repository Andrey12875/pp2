def greet_user(user_name):
    print(user_name)


def show_user_age(user_age):
    print(user_age)


def add_numbers(first_number, second_number):
    result = first_number + second_number
    print(result)


def multiply_numbers(first_number, second_number):
    result = first_number * second_number
    print(result)


def show_profile(user_name, user_age, is_active):
    user_profile = {
        "name": user_name,
        "age": user_age,
        "active": is_active
    }
    print(user_profile)


def show_items(items):
    for item in items:
        print(item)


def check_number(number):
    if number > 10:
        print("asdfg")
    else:
        print("qwert")


def repeat_word(word, count):
    for number in range(count):
        print(word)


def show_coordinates(x_position, y_position):
    coordinates = (x_position, y_position)
    print(coordinates)


def find_biggest_number(numbers):
    biggest_number = max(numbers)
    print(biggest_number)


greet_user("qwer")
show_user_age(18)
add_numbers(5, 7)
multiply_numbers(4, 6)
show_profile("zxcv", 21, True)
show_items(["asdf", "hjkl", "tyui"])
check_number(15)
repeat_word("mnbv", 3)
show_coordinates(10, 25)
find_biggest_number([8, 3, 12, 5])