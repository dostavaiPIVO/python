from string import ascii_uppercase
import random


a = int(input())
stroka = ""
for i in range(a):
    b = random.choice(ascii_uppercase)
    stroka += b
stroka = set(stroka)
print("".join(stroka))
