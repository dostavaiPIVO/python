from tkinter import *

win = Tk()
win.geometry("400x200")
win['bg'] = "yellow"
# win['background'] = "pink"

# ====НАДПИСЬ====
lab = Label(win, text="Сколько бабок сбил?")  # создание
lab.pack()  # размещение
lab['bg'] = "yellow"
lab["foreground"] = "black"  # просто
# lab["foreground"] = "#f4f45b" # hex code
lab.pack()


# ====ОДНОСТРОЧНЫЙ ВВОД====
# ent = Entry(win, width=25,
#             borderwidth=5,
#             font="Arial 12")
# ent.pack()

# ====МНОГОСТРОЧНЫЙ ВВОД====
# txt = Text(win, width=20, height=4, wrap="word")
# txt.pack()

# ====КНОПКА====
# def action():
#     print("бау шлепнул")
#
#
# btn = Button(win, command=action, bg=)
# btn['text'] = "дауби"
# btn.pack()

# ====CheckButton====

# def get_cb():
#     print(cb_val.get())
#
# cb_val = BooleanVar() # хранится значение
# cb = Checkbutton(win,
#                  text="Пользовательское соглашение",
#                  command=get_cb,
#                  variable=cb_val, # привязываем к хранилищу
#                  onvalue=True,
#                  offvalue=False,
#
#                  )
#
# cb.pack()
# cb.select() # .select() - ставит галочку
# cb.deselect() # .deselect() - убрать галочку

# ====Radiobutton====

# def get_rb():
#     print(rb_val.get())
#
#
# rb_val = IntVar()
# rb1 = Radiobutton(win,
#                   text="была одна..",
#                   variable=rb_val,
#                   value=2,
#                   command=get_rb)
# rb1.pack()
#
# rb2 = Radiobutton(win,
#                   text="я стрей",
#                   variable=rb_val,
#                   value=5432,
#                   command=get_rb)
# rb2.pack()

# ====Scale====

# def get_scala(val):
#     print(scala.get()) # первый способ
#     print(val) # второй способ
#
#
# scala = Scale(win,
#               from_=50,
#               to=120,
#               orient=HORIZONTAL,  # ориентация
#               length=300,  # длинна полосы в пикселях
#               tickinterval=10,  # разметка
#               resolution=5,  # шаг
#               command=get_scala)
#
# scala.pack()

# ====PhotoImage====
#
# img = PhotoImage(file="kartinki/ggg.png")
# img_small = img.subsample(3, 3) # .subsample() - уменьшение
# img_big = img.zoom(3, 3) # .zoom - увеличивает
# img_poltora = img.subsample(3, 3).zoom(2, 2)
# lab = Label(win, image=img_poltora)
# lab.pack()

# ====Отступы====
# Label(win, text="Далби", bg="pink").pack()
# Label(win, text="Дауби", bg="lightblue").pack(pady=15, ipady=20)

win.mainloop()
