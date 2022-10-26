import random
while True:
    print("Угадай число")

    try:
        difficult = int(input("введ максимальное число для угадывания-->"))
        if difficult < 1:
            raise Exception
    except Exception:
        print("число больше нуля")
        continue

    mini = 0
    maxi = difficult
    computer_number = random.randint(0, difficult)
    life = 7
    while life > 0:
        try:
            user_number = int(input("Введи число: "))
        except ValueError:
            print("цифрами")
            continue
        if user_number < 0 or user_number > difficult:
            print(f"Введи число от 0 до {difficult}")
            continue
        if computer_number == user_number:
            print("легчайшая 🚬🚬🚬")
            break
        elif computer_number < user_number:
            print("Нужно меньше.")
            maxi = user_number
        else:
            print("Нужно больше.")
            mini = user_number
        print(f">>> Интервал: {mini} – {maxi}")
        life = life - 1
        print("жизней ❤️-", life)
    answer = input("Хочешь продолжить?")
    if answer == "Да":
        continue
    else:
        break