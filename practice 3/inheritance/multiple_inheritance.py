class Walker:
    def walk(self):
        return "asdf"


class Runner:
    def run(self):
        return "qwer"


class Dog(Walker, Runner):
    pass


dog = Dog()
print(dog.walk())
print(dog.run())


class Engine:
    def start(self):
        return "zxcv"


class Wheels:
    def roll(self):
        return "hjkl"


class Car(Engine, Wheels):
    pass


car = Car()
print(car.start())
print(car.roll())


class Reader:
    def read(self):
        return "tyui"


class Writer:
    def write(self):
        return "bnmv"


class Student(Reader, Writer):
    pass


student = Student()
print(student.read())
print(student.write())


class Camera:
    def photo(self):
        return "ghjk"


class Screen:
    def show(self):
        return "vbnm"


class Phone(Camera, Screen):
    pass


phone = Phone()
print(phone.photo())
print(phone.show())


class Width:
    def width(self):
        return 5


class Height:
    def height(self):
        return 7


class Box(Width, Height):
    pass


box = Box()
print(box.width())
print(box.height())


class Cook:
    def cook(self):
        return "lkjh"


class Seller:
    def sell(self):
        return "mnbv"


class Worker(Cook, Seller):
    pass


worker = Worker()
print(worker.cook())
print(worker.sell())


class Sweet:
    def taste(self):
        return "poiuy"


class Round:
    def shape(self):
        return "trewq"


class Apple(Sweet, Round):
    pass


apple = Apple()
print(apple.taste())
print(apple.shape())


class Board:
    def board(self):
        return "cxzv"


class Timer:
    def time(self):
        return 60


class Chess(Board, Timer):
    pass


chess = Chess()
print(chess.board())
print(chess.time())


class Metal:
    def material(self):
        return "asdfg"


class Heavy:
    def weight(self):
        return 8


class Hammer(Metal, Heavy):
    pass


hammer = Hammer()
print(hammer.material())
print(hammer.weight())


class Login:
    def login(self):
        return True


class Delete:
    def delete(self):
        return False


class Admin(Login, Delete):
    pass


admin = Admin()
print(admin.login())
print(admin.delete())