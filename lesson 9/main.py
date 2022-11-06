# # # # import random
# # # # import time
# # # #
# # # # print("время застрелиться")
# # # #
# # # # is_game = "y"
# # # # while is_game == "y":
# # # #     time.sleep(0.5)
# # # #     print("*заряжаем револьвер*")
# # # #     time.sleep(2.5)
# # # #     print("*раскручиваем барабан*")
# # # #     time.sleep(1.5)
# # # #
# # # #
# # # #     # git config --global url. "https://github.com/".instedof git@github.com:
# # # #
# # # #     # git config --global url. "https://".insteadof git://
# # # #
# # # #     # --- если нет прав доступа
# # # #
# # # #
# # # #     print(3)
# # # #     time.sleep(1)
# # # #     print(2)
# # # #     time.sleep(1)
# # # #     print(1)
# # # #     time.sleep(1)
# # # #     print("*выстрел*")
# # # #
# # # #     slots = [1, 2, 3, 4, 5, 6]
# # # #     patron = random.choice(slots) # .choise - случайно выбрать
# # # #     our = random.choice(slots)
# # # #
# # # #     if patron == our:
# # # #         print("ти убит")
# # # #         is_game = "n"
# # # #     else:
# # # #         print("фарт люти")
# # # #         x = input("играем дальше? y - да, n - нет")
# # # #         if x == "n":
# # # #             is_game = "n"
# # #
# # #
# # # # ЦИКЛЫ
# # #
# # # # for
# # # # lst = ["дура", "gul", "genii", "loh"]
# # # # for element in lst:
# # # #     print(element, end="🐷")
# # # #
# # # #
# # # # print()
# # # # for i in range(0, 10):
# # # #     print("я тоже сижу под бомбами")
# # #
# # #
# # # # while
# # # x = 0
# # # while x != 10:
# # #     print(x)
# # #     x += 1 # то же самое что и x = x + 1
#
#
# #
# # word = input("введи слово:")
# # while word: # если слово не равно 0 то работает
# #     print(word)
# #     word = word[:-1]
#
#
# x = int(input("введи циферку:"))
# while x:  # если не = 0 то работает
#     x -= 1 # то же самое что и x = x -1
#     if x % 2 == 0: # если остаток от деления = 0
#         print(x, end=" ")



x = int(input("введи циферку: "))
step = 0
while x != 1:
    step += 1 # то же самое, что step = step + 1
    if x % 2 == 0:
        print(f"{step})", end=" ")
        print(x, "* 3 + 1 =", end=" ")
        x = x // 2
    else:
        print(f"{step})", end=" ")
        print(x, " / 2 =", end=" ")
        x = 3 * x + 1
    print(x)
print("шагов", step)