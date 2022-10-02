# # # # x = ["a","b","c","d","u","f","g","i","j",]
# # # x = "мама мыла раму"
# # # print("строка:", x)
# # # print("первый элемент =", x[0])
# # # print("последний элемент =", x[-1])
# # # print("первые 5 элементов через одного =", x[0:5:2])
# # #
# # # # x = "прювет"
# # # # x[2] = "и" # так нельзяф
# #
# # # temp = x[-1]
# # # index = x.index(temp)
# # # print(index  + 1)
# # # x = input("Введи слово:")
# #
# # # print(len(x))
# # path = "C:/Python3/python.exe"
# # # print("имя файла:", path[-10:])
# # # print("Расщирение:", path [-3:])
# # # print("Имя каталога:", path[3:10])
# # # print("полный путь к каталогу:", path[0:10])
# #
# # path2 = path.split("/")
# # print(path2)
# #
# # print("имя файла:", path2[-1])
# # print("Расщирение:", path2[-1][-3:])
# # print("Имя каталога:", path2[1])
# # print(f"Полный путь к каталогу: {path2[0]}/{path2[1]}")
# chapter_1 = input("Глава 1:")
# page_1 = input("Страница:")
#
# chapter_2 = input("Глава 2:")
# page_2 = input("Страница:")
#
# chapter_3 = input("Глава 3:")
# page_3 = input("Страница:")
#
# print(chapter_1.ljust(15), page_1.rjust(15))
# print(chapter_2.ljust(15), page_2.rjust(15))
# print(chapter_3.ljust(15), page_3.rjust(15))
x = "12'345'678"
# temp = x.split("'")
# print(temp)
# numder = int(temp[0] + temp [1] + temp[2]) -- одно из решений
# print(numder)

# temp = x [0:1] + x[3:6] + x [-3:]
# number = int(temp)
# print(number)
# через .replace
temp = x.replace("'", "")
print(temp)