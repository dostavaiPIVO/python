from tkinter import *

# ЗАДАНИЕ 1

# def knopka(event):
#     message = ent.get()
#     lab["text"] = message
#
# root = Tk()
# root.geometry("400x500")
#
#
# lab = Label(root, text="...")
# lab.pack()
#
# ent = Entry(root)
# ent.bind("<Button-3>", knopka)
# ent.insert(0, "Впиши и ПКМ")
# ent.pack()
#
#
# root.mainloop()

# ЗАДАНИЕ 2
# def hel_lo():
#     user_choise = rb_val.get()
#     if user_choise == 1:
#         lab["text"] = "Hello" + rb1["text"]
#     else:
#         lab["text"] = "Hello" + rb2["text"]
#
# root = Tk()
# root.geometry("400x500")
#
# lab = Label(root, text="Hello")
# lab.pack()
#
# rb_val = IntVar()
#
# rb1 = Radiobutton(root, text="World", variable=rb_val, value=1, command=hel_lo)
# rb1.pack()
#
# rb2 = Radiobutton(root, text="Python", variable=rb_val, value=2, command=hel_lo)
# rb2.pack()
#
# root.mainloop()

# ЗАДАНИЕ 3

def activation():
    if cb_val.get() == True:
        b["text"] = "Активна!"
        b["state"] = "normal"
    else:
        b["text"] = "Не активна!"
        b["state"] = "disabled"

root = Tk()
root.geometry("400x500")

cb_val = BooleanVar()
cb = Checkbutton(root, text="Активатор", variable=cb_val, onvalue=True, offvalue=False,
                 command=activation)

cb.pack()
b = Button(root, text="Не активно!", state="disabled")
b.pack()


root.mainloop()