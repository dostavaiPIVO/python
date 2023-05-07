from tkinter import *

# ЗАДАЧА 1 и 1.1

# root = Tk()
# root.geometry("500x500")
# c = Canvas(root, height=500, width=500, bg="white")
# c.pack(anchor=CENTER)
# second = 0
# img = PhotoImage(file='бамбам.png').subsample(2, 2)
#
# def seconds():
#     global second
#     c.delete("all")
#     second += 1
#     c.create_image(250, 250, image=img)
#     c.create_text(int(c["height"]) / 2, 500 / 2, text=second, font="Arial 50")
#     root.after(1000, seconds)
#     if second == 15:
#         root.destroy()
#
#
# c.create_text(int(c["height"])/2, 500/2,  text=second, font="Arial 50")
# c.create_image(250, 250, image=img)
# root.after(1000, seconds)
#
#
#
# root.mainloop()


# ЗАДАНИЕ 3

root = Tk()
root.geometry("500x500")

c = Canvas(root, height=400, width=400, bg="white")
c.pack()

l = None
p = None


def lkm(event):
    global l
    l = (event.x, event.y)


def pkm(event):
    global p
    p = (event.x, event.y)


def stroitel():
    c.create_line(l[0], l[1], p[0], p[1])


btn = Button(root, text="Построить прямую", command=stroitel)
btn.pack()
c.bind("<Button-1>", lkm)
c.bind("<Button-3>", pkm)

root.mainloop()