# #  lst = [3, 5, -23, 0]
# # print(min(lst))
# # print(max(lst))
# # print(sorted(lst)) # sorted() - сортировка
#
# word_1 = input("Введи первое из двух слово:")
# word_2 = input("Введи второе из двух слово:")
#
# word_1 = word_1.lower() # umenshaem tekst
# word_2 = word_2.lower() # umenshaem tekst
#
# word_1_sorted = sorted(word_1)
# word_2_sorted = sorted(word_1)
#
# if word_1_sorted == word_2_sorted:
#     print("Это анаграммы")
# else:
#     print("Это не анаграммы 🖕")

q1 = input("Сколько хромосом у дотера?\n"
           "a) 9999999, b) 9999999, v) 999999, g) 99999999\n"
           "вводить сюда, специально для дотеров -->")
if q1 == "9999999":
    print("угадал, ты дотер?")
else:
    print("поздровляю ты нормальный человек")
    quit()

q2 = input("когда был представлен первый iphone?\n"
           "a) 2004, b) 2006, v) 2007, g) 2005\n"
           "-->")
if q2 == "2007":
    print("ливай, яблочник")
else:
    print("не угадал, иди учись")
    quit()


q3 = input("хускар нормальный персонаж?\n"
           "a) нет, b) no, v) удалите его из игры, g) я играю на хускаре \n"
           "-->")
if q3 == "удалите его из игры":
    print("харош")
else:
    print("ливай")
    quit()

print("поздровляю вы прошли игру")
print("не приходи сюда больше")








