import easygui
import random

def rock_paper_scissors():
    b="imagess/б.png"
    k="imagess/к.png"
    n="imagess/н.png"
    user=easygui.buttonbox(
        images=[b, k, n],
        choices=("выйти",),
    )

    comp=random.choice([b,k,n])


    if user == b and comp == b:easygui.msgbox(msg="ничьЯ")
    elif user == b and comp == k:easygui.msgbox(msg="ти вийграл, не играй на наге.")
    elif user == b and comp == n:easygui.msgbox(msg="комьютер вийграл, ливай.")
    elif user == k and comp == n:easygui.msgbox(msg="ю вин.")
    elif user == k and comp == k:easygui.msgbox(msg="ничья.")
    elif user == k and comp == b:easygui.msgbox(msg="комьютер вийграл, ливай.")
    elif user == n and comp == n:easygui.msgbox(msg="не чья ?")
    elif user == n and comp == b:easygui.msgbox(msg="комп - бот.")
    else:easygui.msgbox(msg="комьютер вийграл, ливай.")






def guess_the_number():
    chislo = random.randint(1, 100)
    gn = easygui.integerbox(upperbound=100, lowerbound=1, msg="Попробуй отгадать число от 1 до 100!")
    while gn != chislo: # пока не угадаем
        if gn > chislo:
            gn=easygui.integerbox(upperbound=100, lowerbound=1, msg=f"Нет, нужно число меньше чем {gn}", image="imagess/м.png")
        elif gn < chislo:
            gn=easygui.integerbox(upperbound=100, lowerbound=1, msg=f"Нет, нужно число больше чем {gn}", image="imagess/больше.png")
    easygui.msgbox(msg="Ура, победа !",image="imagess/2gis.png")

games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()