from tkinter import *
root = Tk()
root.geometry("550x550")




c = Canvas(root, height=500, width=500, bg="white")
c.pack(anchor=CENTER, expand=True)


# ====== TEXT ======
# c.create_text(10, 10,
#               text="мажор винер",
#               anchor=NW,
#               font="Arial 55 bold",
#               fill="magenta")

# ====== RECTANGLE ======
# c.create_rectangle(10, 10,
#                    150, 150,
#                    fill="yellow",
#                    outline="red",
#                    width=1)



# ====== POLYGON ======
# c.create_polygon(10, 10,
#                  150, 150,
#                  10, 150)

# ====== OVAL ======

# c.create_oval(10, 10,
#               150, 250)


# ====== ARCA ======
# Сектор
# c.create_arc(10, 10,
#              150, 150,
#              extent=45,
#              start=45)

# хорда
# c.create_arc(10, 10,
#              150, 150,
#              extent=45,
#              start=45,
#              style=CHORD)

# дуга
# c.create_arc(10, 10,
#              150, 150,
#              extent=45,
#              start=45,
#              style=ARC,
#              outline="yellow",
#              width=2)


# отрисовка

# c.create_rectangle(10, 10,
#                    150, 150,
#                    fill="yellow",
#                    outline="red",
#                    width=1,
#                    dash="-",
#                    activefill="pink",
#                    activewidth=10)


# event

def bumba(event):
    print(event.x, event.y)

btn = Button(root, text="Кнопочка")
btn.pack()
btn.bind("<Button-3>", bumba)



root.mainloop()