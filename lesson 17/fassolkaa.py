def beans(x:int):  # отнимает фасоль
    global fassol
    fassol -= x


fassol = 20
while True:

    # ход первого игрока
    while True:  # проверк корректности
        first = int(input("1,2 или 3 боба"))
        if first <= 3 and first >= 1:
            break
        else:
            print("введи нормальное число, юморист")
    beans(first)
    if fassol < 1:
        print("второй вин на изи тебя виграл нуба тупого")
        break
    print(fassol)


    # ход второго игрока
    while True:  # проверк корректности
        second = int(input("1,2 или 3 боба"))
        if second <= 3 and second >= 1:
            break
        else:
            print("введи нормальное число, юморист")
    beans(second)
    if fassol < 1:
        print("первый вин, а ты фрик иди гуляй")
        break
    elif fassol == 1:
        print("второй выйграл, ливай")
    else:
        print(f"{fassol}")


