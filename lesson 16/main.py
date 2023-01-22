# LAMBDA функции (анонимные)

# primer1 = lambda a, b: a + b + 1 # lambda функцию поместили в переменную
#
# print(primer1(5, 10))  # вызов функции неотличается от обычного вызова функции
#
# answer = "Д"
# exit_triger = lambda yn: True if yn == "Д" else False # if else в одну строку (гениально так то)
# print(exit_triger(answer))



# LIST COMPREHENSION (генератор списка)

# lst = []
# for i in range(1, 6):
#     lst.append(i)
# print(lst)
#
# lst2 = [i for i in range(1, 6)]
# 1. всегда в []
# 2. for i in ... -> сколько элементов выполнится
# 3. все что перед for -> сам элемент списки


# задача намбер 1 (ёмаё)


# c2f = lambda c: 9/5 * c + 32
# f2c = lambda f: (f-32) * 5/9
# c2k = lambda c: 273.15 + c
# k2c = lambda k: k - 273.15
# f2k = lambda f: c2k(f2c(f))
#
# degree = 203
# print(c2k(degree))  # обращение к лямбда функции


# задача намбер 2 (ёмаё)

# import random
# exit_vihod = lambda yn: True if yn == "д" else False
# while True: # бесконечный цикл (гениально капец)
#     skolko = int(input("сколько кубиков бросаем?"))
#     dice = [random.randint(1, 6) for i in range(skolko)]
#     print(dice)
#     igrok = input("заканчиваем? да - д")
#     print(exit_vihod(igrok))
#     if exit_vihod(igrok) == True:
#         break


# задача намбер 3 (ёмаё)
# from random import choice
#
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
# lst = []
# for i in range(6):
#     lst.append(choice(choice(chars))) # случайный элемент в список добавили на гениалычах кста
# code = "".join(lst)
# ssilka = "https://youtu.be/ozcy6c7TwXw"
# d = {}
# # d = {"https://youtu.be/ozcy6c7TwXw" : "roflan"}
# if ssilka in d:
#     print("эта ссылка уже есть в базе вoт её код ->", d[ssilka])
# else:
#     d[ssilka] = code
#     print("ссылка добавлена вот её код ->", d[ssilka])


# за да чей 4 (чей?)
import math

a = 2
b = 1024
yy1 = lambda a, b : b - a
print(yy1(a, b))

yy2 = lambda a, b : b + a

yy3 = lambda a, b : b / a

yy4 = lambda a, b : b * a

yy5 = lambda a, b : a / b


loloshka = lambda x : -x if x<0 else x
print(loloshka(-5))


logarifm = lambda a, b : math.log(b, a)
print(logarifm(2, 1024))














