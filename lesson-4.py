# def abc(a: int = 5) -> str:  # type hint
#     return a
#
# func = lambda a, b: a + b
# print(func(2, 3))

# Классы. Полиморфизм. Наследование. Инкапсуляция.

# class Human:
#     pi = 3.14  # статический атрибут
#
#     def say(self, fraza):  # публичный метод
#         return fraza
#
#     def __init__(self, vozrast:int=0):  # init -> initialization
#         print("Я пил пива")
#         self.age = vozrast  # динамический атрибут
#         self.money = 0
#
#     def __sad(self):  # приватный метод
#         print("😖")
#
#     def work(self):
#         self.money += 1000
#         self.__sad()  # приватные можно использовать только внутри классов.
#
#     def __call__(self, *args, **kwargs):
#         print(f"Я Антон мне {self.age}, у меня нет {self.money} рублей на микроволновку")
#
#     def __add__(self, other):
#         if type(other) == int:
#             return "мандаринка" * other
#         return "анлак"
#
#
# grisha = Human(vozrast=23)  # создание объекта на основе класса -> init
# print(grisha.say("Привет!"))
# print(grisha.age)  # вывод атрибута
# grisha.age = 50  # меняем атрибут
# grisha()
# print(grisha + 0.0)  #мандаринка
#
# anton = Human(vozrast=14)
# print(anton.say("габела тебе малодой!"))
# anton.work()
# print(anton.money)
# print(anton + 0)  # мандаринка * 0
# print(anton + 2)  # мандари

class Abc:
    def __init__(self):
        self.param = 5

    def komanda(self):
        return "Я - команда"

class Def(Abc):  # наследование (abc - родительский класс)

    def action(self):
        return "Я - играю на тинкере"

a = Abc()
print(a.param)
b = Def()
print(b.param)
print(a.komanda())
print(b.komanda(), b.action())

# print = input
# print("Введи число")
