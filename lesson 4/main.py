# # # # alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТ"
# # # #
# # # # print(alphabet[::-2])  #вывод в обратном порядке
# # # # [start:end:step]
# # # #
# # # # phrase = "gg"
# # # # print(phrase.upper()) #поднять в верхний регистр
# # # # print(phrase.lower()) #опустить в нижний регистр
# # # #
# # # # phrase1 = "Я величайший, я белгородсикй купольщик..."
# # # # print(phrase1.capitalize()) #нормализует текст, в стандартную форму.
# # #
# # # #familiya =input("Фамилия:").capitalize()
# # # # imya =input("Имя:").capitalize()
# # # # otchestvo = input("Отчесво:").capitalize()
# # # # print(familiya, imya[0] + ".", otchestvo[0] + ".")
# # # # print(f"{familiya} {imya[0]}. {otchestvo[0]}.")  #задача 1, выводит инициалы по приколу реал.
# # #
# # # # x = input()
# # # # print(x.lower().count('а')) # кол-во маленьких "а"
# # #
# # # # x = input("Введите фразу, разделяя слова запятыми: ")
# # # # lst = x.split(",")
# # # # lst.pop(0)
# # # # print(lst)  #split - разделить, расколоть.
# # #
# # # #.remove("Вова") - удалить элемент "Вова"
# # # #.pop(3) - удалить элемент под индексом 3
# # #
# # # phrase = input("Введите фразу:")
# # # find = input("Что меняем:")
# # # replace = input("На что меняем:")
# # #
# # # print(phrase.replace(find, replace))
# #
# # # phrase = input("Введите фразу:")
# # # print(phrase.replace("ё", "е"))
# #
# # alphabet = {
# #     " ":" ",
# #     "а":"a",
# #     "б":"b",
# #     "в":"v",
# #     "г":"g",
# #     "д":"d",
# #     "е":"e",
# #     "ё":"yo",
# #     "ж":"zh",
# #     "з":"z",
# #     "и":"i",
# #     "к":"k",
# #     "л":"l",
# #     "м":"m",
# #     "н":"n",
# #     "о":"o",
# #     "п":"p",
# #     "р":"r",
# #
# # }
# #
# # x = input("Введите фразу для перевода:")
# # rus = ""
# # for bukva in x:
# #     rus = rus + alphabet[bukva]+ " "
# # print(rus)
#
# alphabet = {
#     " ":" ",
#     "а":"Арбуз",
#     "б":"Баран",
#     "в":"Виталя",
#     "г":"горох",
# }
#
# x = input("Введи фразу:")
# rus = ""
# for bukva in x:
#     rus = rus + alphabet[bukva]
# print(rus)

email = input("Введите почту:")
print(email.split("@"))
login =email.split("@")[0]
domen = email.split("@")[-1]
print("Логин:", login)
print("Домэн:", domen)

