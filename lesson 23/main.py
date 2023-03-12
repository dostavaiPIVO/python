import random

# class Person:
#     def __init__(self, imya, vozrast):  # магический метод (инициализации)
#         self.name = imya
#         self.age = vozrast
#     def __str__(self):
#         return f"Я {self.name} и мне {self.age} года"
#
# chelovek = Person("Данис", 29)  # создание объекта класса Person
# chelovek1 = Person("Дурачьё", 32)  # создание объекта класса Person
#
# print(chelovek.name)
# print(chelovek1.name)
# print(chelovek)
# print(chelovek1)


# ЗАДАЧА 1

# class Human:
#     def __init__(self, imya, familia, vozrast):
#         self.name = imya
#         self.familia = familia
#         self.age = vozrast
#     # def __str__(self):
#     #     return f"Я {self.name} {self.familia} self.age}"
#
# chelovek = Human("Виталя", "Цаль", 32)
#
# print(chelovek.name, chelovek.familia, chelovek.age)


# ЗАДАЧА 1.1 and 1.2

# class Human:
#     def __init__(self, imya, familia, vozrast):
#         self.name = imya
#         self.familia = familia
#         self.age = vozrast
#     def __str__(self):
#          return f"Имя:{self.name};\nФамилия:{self.familia};\nВозраст:{self.age};"
#     def greet(self):
#         return f"Привет! Меня зовут {self.familia} {self.name}, {self.age}"
# chelovek =Human("Виталя", "Цаль", "32")
# print(chelovek.name, chelovek.familia, chelovek.age)
# # print(chelovek)
# print(chelovek.greet())


#  ЗАДАЧА 2
# list = []
# for i in range(random.randint(5, 10)):
#     list.append(random.randint(2, 5))
# nums = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
# print(nums)

class Human:
    def __init__(self, imya, familia, vozrast):
        self.name = imya
        self.familia = familia
        self.age = vozrast
        self.grades = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
        self.srbal = sum(self.grades)/len(self.grades)

    def __str__(self):
         return f"Имя:{self.name};\nФамилия:{self.familia};\nВозраст:{self.age};"
    def greet(self):
        return f"Привет! Меня зовут {self.familia} {self.name},мне {self.age}"

chelovek = Human("Виталя", "Цаль", "32")
chelovek1 = Human("Серега", "Пиратович", "27")
print(chelovek.grades, chelovek.srbal)



