from user import User

u1 = User(fam="Лагуткин", im="Денис", log="dengut", pas="12345")
u2 = User()

# print(u1.login)
# print(u2.login)
#
# print(u1.surname)
# print(u2.surname)

users = [u1, u2]
l = input("Введи логин: ")
p = input("Введи пароль: ")

for chelovek in users:
    if chelovek.log_in(l, p):
        print("Авторизация выполнена.")
        current = chelovek  # сохраняю текущего пользователя