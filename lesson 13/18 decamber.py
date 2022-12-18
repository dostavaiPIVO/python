# СЛОВАРИ
# dict1 = {"ключ1": 1.2,
#          "ключ2": "папенси",
#          "Якрут": True,
#          "словарь": {"вл1": 1}}  # пример создания словаря
# empty_dictionary1 = {} # 1-й способ создания пустого словаря
# empty_dictionary2 = dict() # 2-й способ создания пустого словаря
#
# print(dict1["словарь"]["вл1"])



# ЦИКЛЫ
# While and For
x = 5
# while x == 5:
#     pass
# while True: # бесконечный цикл
#     print(123)
#
# while False: # ШИЗА ЧЕЛ ЭТО НИКОГДА НЕ СРАБОТАЕТ
#     print("рофлан") # код недосягаем


# FOR
# phrase = "фраза"
# for toyota_supra in phrase: # 1-й способ перебор в переменной
#     print(toyota_supra)

# for jojo in range(5): # сработает 5 раз, от 0 до 4
#  for jojo in range(0, 5):  # то же самое
#     print(jojo)


# МНОЖЕСТВА

# empty_dict= dict()  # единственный способ создания пустого множества
# set1 = {1, 2, 3} # литеральный способ
# print(type(set1))

# set0 = {1, 1, 1, 2} # 1) повторения исключены
# print(set0)
# set00 = {"А", "Б" "Ц"}  # 2) НЕУПОРЯДОЧНЫЙ ТИП ДАННЫХ
# print(set00)
# set = {1, [2, 3]} # список во множестве
# # TypeError -> Нельзя помещать изменяемые типы данных во множество
#
#
# # немутабельные типы данных = неизменемые
# # int, float, bool, str, tuple



# ОПЕРАЦИИ НА МНОЖЕСТВА

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
#
# # объеденение
# print(set1.union(set2)) # объеденение через метод .union
# print(set1 | set2) # то же самое только через оператор |
#
#
# # пересечение
# print(set1.intersection(set2)) # через метод .intersection
# print(set1 & set2) # через амперсанд &
#
# # разность
# print(set1.difference(set2))  # через метод .difference
# print(set1 - set2)
#
# # Симметрическая разность
# print(set1.symmetric_difference(set2)) # через метод .symmetric_difference
# print(set1 ^ set2)



# from random import randint
#
# lst = []
# for _ in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# unique = set(lst)  # список -> множество
# print(f"{len(unique)}шт.: {unique}")



from random import randint

r_start = 0
r_end = 10_000 # то же самое, что и 10000
size = randint(100, 1000)
















