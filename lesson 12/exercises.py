    # a = int(input("a: "))
# b = int(input("b: "))
# lst = []
#
# for aaa in range(a + 1, b):
#     lst.append(aaa ** 2)
# print(lst)


# x = input("Ввод: ")
# # print(x[::-1])  # гениально отзеркалили, но не то
# lst = x.split(" ")
# print(lst)
# lst.reverse()
# print(lst)



# number = ""
# chet = 0
# nechet: int = 0
# lst = []
#
# while number != "end":
#     number = input("Число: ")
#     if number.lstrip("-").isdigit():
#         #  .lstrip("-") - удаляем минус слева
#         number = int(number)
#         lst.append(number)
#     elif number == "end":
#         break  # выход из цикла
#     else:
#         print("Число пожалуста ")
#         continue  # перезапускаем цикл
#
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
#
# print(lst)
# print(f"Четных: {chet}шт.")
# print(f"Нечетные: {nechet}шт.")


lst = [-5, -8, 2, 14, 1]
mini = min(lst)
maxi = max(lst)

# lst.index(mini) - индекс значения
# lst[] - само значение

lst[lst.index(mini)], lst[lst.index(maxi)] = lst[lst.index(maxi)], lst[lst.index(mini)]
print(lst)





