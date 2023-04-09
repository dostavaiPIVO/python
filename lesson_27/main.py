# import math
# zemlekopi = 1.5
# x = (math.ceil(zemlekopi))
# print(x)



# # ЗАДАЧА 1
# c1 = input("Введите первый цвет -").strip().lower()
# c2 = input("Введите второй цвет -").strip().lower()
#
# c = ("красный", "желтый", "синий")
#
# if c1 not in c or c2 not in c:
#     print("введен недопустимый цвет!")
#
# if c1 == c[0] and c2 == c[1] or c1 == c[1] and c2 == c[0]:
#     print("Оранжевый")
#
# if c1 == c[0] and c2 == c[2] or c1 == c[2] and c2 == c[0]:
#     print("Фиолетовый")
#
# if c1 == c[1] and c2 == c[2] or c1 == c[2] and c2 == c[1]:
#     print("Зеленый")
# else:
#     print(с1)




# ЗАДАЧА 2

# first_lesson = input("начало первого урока")
# len_lesson = int(input("длительность урока"))
# break_time = int(input("длительность перемен"))
# lesson_count = int(input("кол-во уроков"))
#
# hours, minutes = first_lesson.split(":")
# hours, minutes = int(hours), int(minutes)
# time = hours * 60 + minutes
#
# for i in range(lesson_count):
#     print(f"{i+1} урок:", end="")
#     print(f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')} - ", end="")
#     time += len_lesson
#     hours = time // 60
#     minutes = time % 60
#     print(f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')}")
#     time += 10
#     hours = time // 60
#     minutes = time % 60




# ЗАДАЧА 3

kol_vo_zombi = int(input("Сколько зомби было к началу расчёта:"))
skolko_zarazit = int(input("Сколько каждый может заразить:"))
day = int(input("На который день делаем расчёт:"))
print(f"1 день:{kol_vo_zombi}")
for i in range(2, day + 1):
    kol_vo_zombi = kol_vo_zombi * skolko_zarazit + kol_vo_zombi
    print(f"{i} день:{kol_vo_zombi}")
