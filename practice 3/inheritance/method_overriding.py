class Animal:
    def sound(self):
        return "asdf"


class Dog(Animal):
    def sound(self):
        return "qwer"


dog = Dog()
print(dog.sound())


class Vehicle:
    def move(self):
        return "zxcv"


class Car(Vehicle):
    def move(self):
        return "hjkl"


car = Car()
print(car.move())


class Person:
    def role(self):
        return "tyui"


class Student(Person):
    def role(self):
        return "bnmv"


student = Student()
print(student.role())


class Device:
    def power(self):
        return False


class Phone(Device):
    def power(self):
        return True


phone = Phone()
print(phone.power())


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def area(self):
        return 25


square = Square()
print(square.area())


class Worker:
    def salary(self):
        return 100


class Manager(Worker):
    def salary(self):
        return 200


manager = Manager()
print(manager.salary())


class Food:
    def price(self):
        return 10


class Apple(Food):
    def price(self):
        return 15


apple = Apple()
print(apple.price())


class Game:
    def level(self):
        return 1


class Chess(Game):
    def level(self):
        return 5


chess = Chess()
print(chess.level())


class Tool:
    def use(self):
        return "ghjk"


class Hammer(Tool):
    def use(self):
        return "vbnm"


hammer = Hammer()
print(hammer.use())


class Account:
    def access(self):
        return "lkjh"


class Admin(Account):
    def access(self):
        return "mnbv"


admin = Admin()
print(admin.access())