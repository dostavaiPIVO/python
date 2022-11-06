# import random   # подтянуть в проэкт библиотеку
# import random as r  # r = random
#
# print(random.randint(0, 100))   # 0 <= x <= 100
# print(r.randint(0, 100))

# from random import*  # импортировать все из модуля (ЭТО ПЛОХО)
# print(randint(0, 100))

# import random as r
# lst = [0, 1, 2, 3, 4, 5]
# print(r.choice(lst))  # random.choice - выбрать одно случайное
# r.shuffle(lst)  # random.shuffle - перемешать содержимое
# print(lst)

import turtle
screen = turtle.Screen()  # экран
t = turtle.Turtle()  # черепашка

# t.forward(500)  # fd
# t.back(100)  # bk
horizontal = 200
vertical = 100
t.pensize(6)  # размер пера в пикселях
t.color("red", "yellow")
t.shape("turtle")
t.speed(1)
# 1 - # медленно
# 10 - # очень быстро
# 0 - # максимальная скорость
t.begin_fill()
t.fd(horizontal)
t.right(90)  # повернуть на 90 градусов на право
t.fd(vertical)
t.right(90)
t.fd(horizontal)
t.rt(90)  # rt = right
t.fd(vertical)
t.rt(90)
t.end_fill()
 #t.speed(2)
t.penup()  # поднять перо
t.goto(120, -40)
t.pendown()  # опустить перо
t.fd(30)
t.circle(30)  # круг с диаметром 30 пикселей
t.write("Movavi", font=("Arial Black", 50, "normal"), align="center")

screen.exitonclick()  # выйти по клику