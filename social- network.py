class User:
    def __init__(self, imya, parol, login):
        self.name = imya
        self.password = parol
        self.nickname = login
        self.followers = []  # кто на тебя подписан
        self.subscribers = []  # на кого ты подписан
        self.session = False

    def change_pas(self):
        if input("Введите старый пароль: ") == self.password:
            self.password = input("Введите новый пароль: ")
            print("Пароль был успешно сменен ✔")
        else:
            print("Неверно. Отказано.")

    def authorize(self):
        while True:
            if not self.session:  # если не вошел
                if input("Логин:") == self.nickname and \
                        input("Пароль:") == self.password:
                    self.session = True
                else:
                    print("Попробуй еще раз.")
            else:  # вошел = сидишь в аккаунте
                print("\n" * 50)
                input("Что будем делать?")


u1 = User("Антошка", "123", "gigaFID")
u2 = User("Илюша", "4545", "TopKerry")
# u1.change_pas()
u2.authorize()
