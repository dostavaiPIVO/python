# ЗАДАЧА 2 (БЕЗ ЦИКЛА)

# word = input().capitalize()
#
# x = ["Никита", "Екатерина", "Андрей", "Андрей", "Анастасия", "Арсалан",
#      "Наталья", "Тимур", "Григорий", "Евгений", "Анастасия",  "Екатерина",
#      "Андрей", "Евгения", "Анастасия", "Герман", "Тимур", "Григорий",
#      "Арсалан", "Ярослава", "Есения", "Даниил", "Данил", "Андрей", "Никита"]
#
# a = x.count(word)
#
# print(a)


# ЗАДАЧА 2 (С ЦИКЛОМ)

word = input().capitalize()

x = ["Никита", "Екатерина", "Андрей", "Андрей", "Анастасия", "Арсалан",
     "Наталья", "Тимур", "Григорий", "Евгений", "Анастасия",  "Екатерина",
     "Андрей", "Евгения", "Анастасия", "Герман", "Тимур", "Григорий",
     "Арсалан", "Ярослава", "Есения", "Даниил", "Данил", "Андрей", "Никита"]

count = 0
for i in x:
     if i == word:
          count += 1

print(count)
