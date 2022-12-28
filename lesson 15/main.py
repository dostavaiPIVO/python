# множества > подмножества и надмножества

# nad = {1, 2, 3}
# s = {0, 1, 2 ,3}
# pod = {1, 3}
# miss = {4, 5}
#
# if miss < s:
#     print("ето подмножество S")




# person1 = {"Python", "C#", "Java"}
# person2 = {"YoptaScript", "Kotlin", "BrainFuck", "C++", "Python"}
#
# if person1 < person2:
#     print("Второй крутой. Он знает стек первого")
# elif person2 < person1:
#     print("Первый крутой. Он знает стек второго")
# else:
#     print("Стеки разработки отличаются")



#ФУНКЦИИ

# def roflan_pominki():  # обозначили функцию (зачем?)
#     print("5")
#     print("4")
#     print("3")
#     print("2")
#     print("1"
#
# roflan_pominki() # вызов функции (еьать удобно)


# def koren(number, stepen):   # функция с двумя аргументами (типо пруфы афигеть)
#     return number ** (1/stepen)  # возвращение результата
#
#
# print(koren(27, 3))


# Первый задача.
# def roflan(spisok):
#     s = sorted(l)
#     if s == spisok:
#         return True
#
# l = [1, 6, 5]
# # roflan(spisok=l)
# if roflan(l):
#     print("отсортированно")
# else:
#     print("ливай")


# задача 2

# def find_longest(words):
#     chisla = []
#     for iek in words:
#         chisla.append(len(iek)) # добавляем в список длинну каждого слова
#     maxi = max(chisla) # максимальная длинна из списка
#     bogdan = chisla.index(maxi) # индекс наибольшей длинны
#     return words[bogdan]
#
#
#
# spisok = ["да", "три", "двенцадцать", "arthas"]
# print(find_longest(words=spisok))


# задача 3
#
# def min_max(spisok):
#     mini, maxi = spisok[0], spisok[0]
#     for i in spisok:
#         if i > maxi: # нахождение нового максимума
#             maxi = i # запись нового максимума
#         if i < mini: # нахождение нового минимума
#             mini = i # запись нового минимума
#     return {'максимум': maxi, 'минимум': mini}
#
# l = [18, 44, 34, 52]
# print(min_max(spisok=l))




# задача 4

# def zip_longest_sum(l1, l2):
#     if len(l1) != len(l2): # если разные длины
#         if len(l1) > len(l2): # если 1-й список больше
#             for index in range(len(l2)): # проходимся во второму списку
#                 l1[index] += l2[index] # складываем элементы
#                 return l1
#         else: # если второй список длинее
#             if len(l2) > len(l1): # если 2-й список больше
#                 for index in range (len(l1)): # проходимся по первому списку
#                     l2[index] += l1[index] # складываем элементы
#                 return l2 # ответ во втором списке
#
# lst1 = [10, 20, 30, 40, 50]
# lst2 = [5,6,7]
#
# print(zip_longest_sum(lst1, lst2))





# задача 5 (так то 1 но хз)


# def prime(number):
#     for i in range(2, (number + 1)):
#         if i == number:
#             return True
#         if number % i == 0:
#             break
# print(prime(523))




