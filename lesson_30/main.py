from tkinter import *


root = Tk()
root.geometry("500x500")

# =============== Listbox ================
# 1 способ

# lst = ["Первый", "Второй", "Пятнадцать"]
# listbox = Listbox(root)
# listbox.pack()
#
# for elem in lst:
#     listbox.insert(END, elem)

# 2 способ

# lst = ["Первый", "Второй", "Пятнадцать"]
# lst_tk = StringVar(value=lst) # получаем кортеж
# lstbox = Listbox(root, listvariable=lst_tk, selectmode=EXTENDED)
# lstbox.pack()
#
# def fu(pelmeni):
#     for ind in lstbox.curselection(): # current = текущий
#         print(lst[ind])
#
# lstbox.bind('<<ListboxSelect>>', fu)


# btn = Button(root, text="Вывести", command=fu)
# btn.pack()




# ==== Messagebox ====
# from tkinter import messagebox
# messagebox.showinfo("обнял, на два пива променял", "Ты знаешь теперь.")
# messagebox.showerror()
# messagebox.showwarning()


# ==== .pack() ====

# btn = Button(root, text="бiмба")
# btn.pack(anchor=SW, expand=True)
# btn.pack(fill=BOTH, expand=True)
# btn1 = Button(root, text="бiмба")
# btn1.pack(pady=50)
# btn2 = Button(root, text="бiмба")
# btn2.pack(pady=50)



# ==== .grid() ====
# ряд = row
# столбик = column
# btn1 = Button(root, text="бiмба1")
# btn1.grid(column=0, row=0)
#
# btn2 = Button(root, text="бiмба2")
# btn2.grid(column=1, row=0)
#
# btn3 = Button(root, text="бiмба3")
# btn3.grid(column=2, row=0, rowspan=2, sticky=NS)
#
# btn4 = Button(root, text="бiмба4")
# btn4.grid(column=0, row=1, columnspan=2, sticky=EW)



# ==== .place() ====
# btn1 = Button(root, text="Кноп очка")
# btn1.place(x=10,y=10)



# ==== .after() ====

# def fu():
#     print("опа")
#     root.after(1000, fu)
#
# root.after(3000, fu)



# ==== .bind() ====

# def fu(pelmeni):
#      print("что")
#
# btn1 = Button(root, text="бамбоня")
# btn1.pack()
# # btn1.bind("<Enter>", fu) # при наведении мышкой
# # btn1.bind("<MouseWheel>", fu) # кручение колеса мышки
# # btn1.bind("<FocusIn>", fu) # фокусировка(tab)
# btn1.focus_set()
# # btn1.bind("<Return>", fu) # enter
# btn1.bind("<h>", fu) # h
# btn1.bind("<Shift-Up>", fu) # shift + up



# ==== .set() ====

# rb_val = IntVar()
# print(rb_val.get())
# rb_val.set(5) # установить значение
# print(rb_val.get())




# ==== .show() ====

# Entry(root, show="*").pack()




root.mainloop()