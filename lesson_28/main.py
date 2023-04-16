from tkinter import *  # импортируем всё

def h_ell_o(event):
    message = ent.get() # прием значений из Entry
    ent.delete(0, END) # очистить значение
    print(message)

root = Tk()  # создание/инициализация
root.geometry("500x400") # размеры ставим окна
root.title("Я русский")
# root.configure(bg=)
root["bg"] = "lightpink " # фон окна


lab = Label(root, text="Данил предатель") # надпись
lab.pack() # размещаем элементы(по порядку)

# lab["background"] = "grey"
# lab["foreground"] = "lightblue"
lab["bg"] = "black" # ключевым словом
lab["fg"] = "#fb32d1" # hex цвет
# lab["font"] = 20 # 1: размер шрифта
# lab["font"] = "Arial 20 bold" # мультизначение строчкой
lab["font"] = ("Arial", "20", "bold", "italic", "underline", "overstrike") # мультизначение картежа
lab["height"] = 8
lab["width"] = 18

btn = Button(root, text="нажми если Данил какашка необразованная",
             bg="lightgreen",
             font=20, # размер шрифта
             #command=h_ell_o
             )
btn.pack()
btn.bind("<Button-1>", h_ell_o)
# Button-1 = ЛКМ
# Button-3 = ПКМ
# Double-Button-3 = ПКМ # два раза нажать типо

ent = Entry(root,
            width=20, # ширина
            font=20,  # размер шрифта
            bd=10) # размер окна
ent.pack()

txt = Text(root,
           width=20,
           height=5,
           wrap="word")
# wrap:
# word - перенос по словам
# char - посимвольный
# none - без переноса (в однустроку)
txt.pack()


root.mainloop() # отрисовка окна
# ПОСЛЕ mainloop() НЕ ЧЕГО НЕ ПИШЕМ