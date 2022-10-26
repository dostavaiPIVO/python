# # # # # # ZeroDivisionError: division by zero
# # # # # # x = 7/0
# # # # #
# # # # # x = 15 + "a"
# # # # #
# # # # # assert summa([1, 2]) == 3
# # # # # assert summa([1, 2]) == 4
# # # # #
# # # # #
# # # # #  NameError
# # # # #  print(x)
# # # #
# # # # try:
# # # #     div = int(input("введи число для деления-->"))
# # # #     x = 5/div
# # # # except ZeroDivisionError:  # обработка деления на ноль
# # # #     print("ошибки при делении на ноликс")
# # # # # except Exception: # обработка любой ошибки
# # # # #     print("oshibkka!")
# # # # except ValueError:
# # # #     print("цифру идиот")
# # # # else: # если ошибок не было
# # # #     print("по кайффу")
# # # # finally: # finally - сработает всегда
# # # #     print("потестил!")
# # # #
# # # #
# # # # print(" ya srabotal")
# # #
# # # lst = []
# # # try:
# # #     f = open("roflan.txt")  # файл помещен  в f
# # # except FileNotFoundError:
# # #     print("где файл то гений?❔")
# # # else:
# # #     try:
# # #         for line in f:  # для каждой строчки в файле
# # #             lst.append(int(line))  # добавить в список число
# # #     except ValueError:
# # #         print("хочу онли ЦИФРЫ")
# # #     else:
# # #         print("чих пых на кайфе🚬")
# # #     finally:
# # #         f.close()
# # #     print(lst)
# # #
# # #
# # #
# # #
# # #
# # #
# #
# #
# # try:
# #     x = 5/0
# # except ZeroDivisionError as error_message:
# #     print("у тебя тут ошибочка", error_message)
#
#
# x = input("я чих пых если че:").lower().strip()
# try:
#     if x == "нет":
#         raise Exception("врешь") # raise - вызов ошибки
# except Exception:
#     print("da")
#

try:
    x = 5/0
except ZeroDivisionError:
    pass # затычка, нечего

if 5 == 2:
    pass


