# print("=" * 50)
# print(list("a" + "b"))

# x = "Антон"
# print(x.index("н"))
# print(x.replace("Ан", ""))
# print(x.strip("но"))  # убирает символы лево-право
# print(x.split("н"))
# print("ПаПиЧ идИ УчисЬ ИГраТь".capitalize())
# print("ПаПиЧ идИ УчисЬ ИГраТь".title())
# print("Алекснадр"[::-1]) # slice

# for pelmeni in range(5):
#     print(pelmeni)
#     break


# Задачи

# big_name = "Данил (гигант)"
# name = "Арсений"
# vosrast = 15
# highest = 267
# x = int(input())

# print(f"{name} ты ниже {big_name} на {highest - x} сантиметров") 

# c1 = input()
# c2 = input()

# if c1 == "красный" and c2 == "синий":
#     print("фиолетовый")
# elif c1 == "красный" and c2 == "желтый":
#     print("оранжевый")
# elif c1 == "синий" and c2 == "желтый":
#     print("зеленый")
# elif c1 == "синий" and c2 == "красный":
#     print("фиолетовый") 
# elif c1 == "желтый" and c2 == "красный":
#     print("оранжевый")
# elif c1 == "желтый" and c2 == "синий":
#     print("зеленый")
# elif c1 == "красный" and c2 == "красный":
#     print("красный")
# elif c1 == "желтый" and c2 == "желтый":
#     print("желтый")
# elif c1 == "синий" and c2 == "синий":
#     print("синий")
# else:
#     print("введены неверние цвета")


#task323
# x1 = int(input())
# x2 = int(input())

# for i in range(x1, x2+1):
#     print(i**3)



# task42
# x1 = 1
# x = int(input())

# for i in range(x1, x+1):
#     x1 *= i
#     print(x1)


# task 213
# x = int(input())
# uvel = int(input())
# days = int(input())

# for i in range(1, days+1):
#     x = x *(1 + (uvel/100))
#     print(i, x)
    
    
    

# task21
# x = [7, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]
# print("+{}({}{}{}){}{}{}-{}{}-{}{}".format(*x))


# task1231
# stroka  = ""
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# y = "THE SUN OLD YUPPY ASDBC"
# for i in y:
#     if i in alphabet:
#         stroka += str(alphabet.index(i) + 1)+" "
# print(stroka)


# task124

z = "abcdefg"
if len(z) % 2 == 1:
    z += "_"
    
for i in range(0, len(z), 2):
    print()

    
    