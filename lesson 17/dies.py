import random

kolichestvo = int(input("напишите сколько костей бросаем:"))
slovar = {}
for i in range(kolichestvo, kolichestvo * 6 + 1):
    slovar[i] = 0

print(slovar)