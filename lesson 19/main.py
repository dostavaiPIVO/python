alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_ru2 = alphabet_ru[::-1]
alphabet2 = alphabet[::-1]
phrase=input("введи сообщение на английском, а я зашифрую на шифр Атбаша ")
phrase2 = ''
for i in phrase:
    if i.upper() in alphabet_ru:
        if i.isupper():
            indx = alphabet_ru.index(i)
            bukva = alphabet_ru2[indx]
        else:
            indx = alphabet_ru.index(i.upper())
            bukva = alphabet_ru2[indx].lower()
        phrase2 = phrase2 + bukva
    elif i not in alphabet:  # если не буква(дословно:"ЕСли элемента нет в строке alphabet"
        phrase2 += i
    elif i.upper() in alphabet:
        if i.isupper():
            indx = alphabet.index(i)
            bukva = alphabet2[indx]
        else:
            indx = alphabet.index(i.upper())
            bukva = alphabet2[indx].lower()
        phrase2 = phrase2 + bukva
print(phrase2)

