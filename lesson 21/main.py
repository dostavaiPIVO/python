# f = open("file.txt", "w", encoding="utf-8")
# f.write("мочи их дахао, вали их дахао.")
# f.close()


# try:
#     f = open("filex.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("поймал лоха")


# try:
#     x = int(input("введи число: "))
#     print(10/x)
# except ValueError:
#     print("ты дегенерат мен, я цифри хочу")
# except ZeroDivisionError:
#     print("я запрещаю вам делить на ноль")
# else: # когда не было исключений
#     print("ты реал не туп мен")
# finally: # в любом случае
#     print("я все")


# raise  # кароче ми можем вызывать ошибки для бана дэбиков

# x = input("введи имя друга: ")
# try:
#     if x == "Данил":
#         raise NameError("ненене это имя Дауна на наге")
# except NameError as pelmeni:
#     print("жалко что у тебя есть такой друг.", pelmeni)


#  ЗАДАЧА 1

#
# def sr_ar():
#     s = 0
#     k = 0
#     for number in text:
#         try:
#             s += int(number)
#         except ValueError:
#             print("найдено не число:", number)
#         else: # если число
#             k += 1
#
#     # print(s)
#     # print(k)
#
#     if k == 0:
#         return "чисел не было найдено"
#     return round(s/k, 2)
#
#
# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файла нет, не нашел я его.")
# text = f.read().split()
# f.close()
#
# print(sr_ar())


# ЗАДАЧА 5

# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файла нет, не нашел я его.")
# text = f.readlines()
# print(f"Строк: {len(text)}")
# full_text = " ".join(text).replace("\n", " ")
# #print(full_text)
# words = full_text.split()
# print(f"слов:{len(words)}")
# symvols = full_text.replace(" ", " ")
# #print(symvols)
#
# print(f"символов:{len(symvols)}")
#
# f.close()


# ЗАДАЧА 6
#
# word = input("Какое слово ищем?: ")
#
# try:
#     f = open("file.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файла нет, не нашел я его.")
# text = f.read()
# f.close()
#
# print(text.count(word))




# ЗАДАЧА 7

try:
    f = open("file.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("файла нет, не нашел я его.")
text = f.read()
f.close()

numbers = text.split()
print(numbers)
p = 1
for i in numbers:
    p *= int(i)
print(p)



