# class Human:
#     def __init__(self):  # инициализация (магический метод)
#         self.height = 993  # public данные
#         self.__money = 0.3  # private данные
#     def zdarova(self):  #  обычный(public) метод
#         return "Усиленно приветствую"
#
#     def ipotek(self):
#         if self.__money > 50 and self.__normal_height():  # юзаем private (внутри класса)
#             return True
#         else:
#             return False
#
#     def __normal_height(self):  # private метод
#         if 100 < self.height < 200:
#             return True
#
#
#
#
#
#
# chelovek = Human()
# # print(chelovek.height)  # вызов атрибута
# # print(chelovek.zdarova())  # вызов метода
#
# print(chelovek.height)  # public можно выводить
# chelovek.height += 7  # public можно менять
#
# # print(chelovek.__money)  # private нельзя выводить
# # chelovek.__money = 5  # private(public) можно менять? (обманка короче)
# # chelovek.__money = chelovek.__money + 5  # private НЕ МОЖНО менять? (обманка короче)
# # print(chelovek.__money)
#
# chelovek._Human__money += 5  # все-таки можно менять (но осторожно)


# ЗАДАЧА 1

# class Car:
#     def __init__(self):
#         self.status = False
#     def start(self):
#         if not self.status:
#             return "Автомобиль заведен"
#         else:
#             return "и так заведена гонка"
#     def off(self):
#         if  self.status:
#             return "Автомобиль заглушен"
#         else:
#             return "и так заглушен"
#     def color(self, color):
#         self.color = color
#     def type(self, type):
#         self.type = type
#     def age(self, age):
#         self.age = age
#
# f = Car()
# f.age("2001")
# f.color("Черный")
# f.type("Хечбек")
# print(f.start(), f.off())

#  ЗАДАЧА 2

# import string
#
# class Alphabet:
#     def __init__(self):
#         self.__lang = "eng"
#         self.__letters = string.ascii_lowercase
#     def print(self):
#         return self.__letters
#
#     def letters_num(self):
#         return len(self.__letters)
#
# a = Alphabet()
# print(a.print())
# print(a.letters_num())


#  ЗАДАЧА 3

import datetime

class Time:

    def __init__(self):
        self.__h, self.__m, self.__s = datetime.datetime.now().strftime("%H:%M:%S").split(":")
        self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)

    def hour(self):
        self.__h += 1
    def vivod(self):
        return f"{str(self.__h).rjust(2, '0')}:{str(self.__m).rjust(2, '0')}:{str(self.__s).rjust(2, '0')}"
    def min(self):
        self.__m += 1
    def sec(self):
        self.__s += 1


vremia = Time()
vremia.hour()
print(vremia.vivod())