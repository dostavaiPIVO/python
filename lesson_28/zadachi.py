from tkinter import *


# ЗАДАЧА 1

#
# root = Tk()
# root.geometry("100x300")
#
# text = Label(root, text="грин")
# text.pack()
# ent = Entry(root,
#             width=20)
# ent.pack()
#
# btn1 = Button(root,
#               width=30,
#               bg="red")
# btn1.pack()
#
#
# btn2 = Button(root,
#               width=30,
#               bg="orange")
# btn2.pack()
#
#
# btn3 = Button(root,
#               width=30,
#               bg="yellow")
# btn3.pack()
#
#
# btn4 = Button(root,
#               width=30,
#               bg="green")
# btn4.pack()
#
#
# btn5 = Button(root,
#               width=30,
#               bg="lightblue")
# btn5.pack()
#
#
# btn6 = Button(root,
#               width=30,
#               bg="blue")
# btn6.pack()
#
#
# btn7 = Button(root,
#               width=30,
#               bg="purple")
# btn7.pack()
#
# root.mainloop()


# ЗАДАЧА 2
#
# def mama():
#     message = ent.get() # прием из Entry
#     ent.delete(0, END) # очистка Entry
#     message1 = txt.get(0.0, END)  # очистка Text
#     txt.delete(0.0, END) # прием из Txt
#     print(f"От пользователя: {message}\nКомментарий - {message1}")
#
#
# root = Tk()
# root.geometry("400x300")
# root["bg"]="lightgrey"
# lb = Label(root, text="Ваш адрес:", bg="wheat")
# lb.pack()
#
# ent = Entry(root, width=15, bd=5, bg="wheat")
# ent.pack()
#
# lb2 = Label(root, text="Комментарий:", bg="lightgrey")
# lb2.pack()
#
# txt = Text(root, width=25, height=10)
# txt.pack()
#
# btn = Button(root, text="Отправить", width=15, bg="lightblue", command=mama)
# btn.pack()
#
#
# root.mainloop()


# ЗАДАЧА 3

def italic(one):
    lab["font"] = lab["font"].replace(" italic", "")
    lab["font"] += " italic"

def bold(two):
    lab["font"] = lab["font"].replace(" bold", "")
    lab["font"] += " bold"

def base(three):
    lab["font"] = lab["font"].replace(" bold", "").replace(" italic", "")


root = Tk()

lab = Label(root, text="Привет")

lab["font"] = "Arial 15"
lab.pack()


lkm = lab.bind("<Button-1>", bold)
pkm = lab.bind("<Button-3>", italic)
lkm2 = lab.bind("<Double-Button-1>", base)

root.mainloop()
