# # # # # # # x = 7
# # # # # # #
# # # # # # # if x >= 10: # больше либо равно.
# # # # # # #     print("Я сработал!")
# # # # # # # else:
# # # # # # #     print("Ну я тоже сработал")
# # # # # # #
# # # # # # # phrase = "я гений"
# # # # # # # if phrase == "ya genii": #р авно ли
# # # # # # #     print("Мы гении!")
# # # # # # #
# # # # # # # game = "dota2"
# # # # # # # if game != "brawl stars":# не равно
# # # # # # #     print("ну можно и поиграть")
# # # # # # x = 7
# # # # # #
# # # # # # if x >= 10 and (x == 0 or x == 666):
# # # # # #     print("Я не сработаю гений!")
# # # # # # else:
# # # # # #     print("Ну я тоже сработал")
# # # # #
# # # # # number = int(input("Введи число: "))
# # # # # if number > 0:
# # # # #     print("Положительное")
# # # # # elif number == 0:
# # # # #     print("Нулик")
# # # # # else:
# # # # #     print("Отрицательное")
# # # #
# # # #
# # # # #
# # # # year = int(input("Введи год:")) #високосный ли год рофлан калькулятор
# # # # if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
# # # #     print("изи вин")
# # # # else:
# # # #     print("гг тима раков")
# # #
# # # number_1 = int(input("Введи первое число:"))
# # # operation = input("Введи операцию(-,+,*,/):").strip() # ввод операции, .strip убирает пробелы
# # # number_2 = int(input("Введи второе число:"))
# # # lst = ["-", "+", "*", "/"] # допустимые значения
# # #
# # # if operation in lst: # если операция есть в списке
# # #     if operation == "-": # если минус
# # #         print(number_1 - number_2)
# # #     elif operation == "+": # если плюс
# # #         print(number_1 + number_2)
# # #     elif operation == "*": # если умножить
# # #         print(number_1 * number_2)
# # #     else: # в других случаях
# # #         print(number_1 / number_2)
# # #
# # number_1 = int(input("Введи число:"))
# # number_2 = int(input("Введи число:"))
# # number_3 = int(input("Введи число:"))
# #
# # counter_pol = 0 # счетчик положительных
# # counter_otr = 0 # счетчик отрицательных
# # # проверка первого числа
# # if number_1 < 0:
# #     counter_otr += 1 # прибавить к отрицательным
# # else:
# #     counter_pol += 1 # прибавить к положительным
# # # проверка второго числа
# # if number_2 < 0:
# #     counter_otr += 1 # прибавить к отрицательным
# # else:
# #     counter_pol += 1 # прибавить к положительным
# # # проверка третьего числа
# # if number_3 < 0:
# #     counter_otr += 1 # прибавить к отрицательным
# # else:
# #     counter_pol += 1 # прибавить к положительным
# #
# #     print("Положительных:", counter_pol)
# #     print("Отрицательных:", counter_otr)
# #
# #
#
#
#
# number_1 = int(input("Введи one число:"))
# number_2 = int(input("Введи two число:"))
# number_3 = int(input("Введи three число:"))
#
# lst = [number_1, number_2, number_3]
#
# maxi = max(lst)
# mini = min(lst)
# print("минимальное:", mini)
# print("максимальное", maxi)
#






ticket = input("Введи номер билета(6 знаков):")
if len(ticket) == 6 and ticket.isdigit(): # .isdigit - число ли это (в формате str)
    first_half = ticket[:3] # сохраняем первые 3 числа
    last_half =  ticket[-3:] # сохраняем последние 3 числа

    first_sum = first_half[0] + first_half[1] + first_half[2] # прибавим 1, 2 и 3 цифры
    last_sum= first_half[0] + first_half[1] + first_half[2] # прибавим 1, 2 и 3 цифры

    if first_sum == last_sum:
        print("Повезло тебе бродяга, счастливый билет.")
    else:
        print("ливай с жизни бездарь.")
else: # если ввод некоректный
    print("иди учись, безграмотный. И не приходи сюда больше.")


