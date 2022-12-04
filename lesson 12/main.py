# мутабельность
# мутабельные - изменяемые
# немутабельные - неизминяемые
# x = "mavavi"
#  x[1] = "о"  # так низя
# x = "movavi"


# списки []
# lst = ["один", "два", "травокрыс"]
# lst.append("спинер")  # добавляем нови элемент - .append()
# lst.pop(0) # .pop() - удалить по индексу
# lst.remove("два")  # .remove() - удалить по значению

# lst = [0, 3, 5, -2, 1]
# lst.reverse()  # .reverse() - отразить, перевернуть
# print(lst)

# lst1 = [0, 1, 2]
# lst2 = [3, 4, 5]
# lst1.extend(lst2) # .extend() - расширить
# print(lst1)

# lst = [1, 2] # [1, 2] -> [1 , 1.5, 2]
# lst.insert(1, 1.5) # .insert() - вставить по индексу

# lst = ["не пустота"] # ["не пустота"] -> []
# lst.clear() # .clear() - очистка

# lst = [0, 4, 2, -5, 1]
# lst.sort() # .sort() - сортировка
# lst.sort(reverse=True)  # reverse=True от меньшего к большему
# print(lst)

# КОРТЕЖ
# tup = (1, 2, 3)
# # tup = 1, 2, 3
# # tup = 1,
# print(max(tup))
# print(min(tup))

# list1 = ["A", "B", "C"]
# list2 = ["1", "1", "2"]
# couple = zip(list1, list2)  # zip() - функция объеденения по индексу
# print(couple)
#
# for drovka in couple:
#     print(drovka)

from collections import namedtuple

citizen = namedtuple("житель", "имя возраст статус какую_группу_уважаешь")
alex = citizen(имя="Леха Денжер", возраст="27", статус="Порося", какую_группу_уважаешь="Аллу Пугачеву")

print(alex.имя)
print(alex.какую_группу_уважаешь)
print(alex.статус)

print(alex)





