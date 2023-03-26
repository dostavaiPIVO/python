# class Human:
#     location = "Новосибирск" # public static
#     # __location = "Секрет" # private static
#     def __init__(self, rost=24, ves=12): # __magic__
#         self.height = rost # public dynamic
#         self.__weight = ves # private dynamic
#         self.otkuda = Human.location # использование статики
#
#     def __private(self):
#         pass
#
#     def public(self):
#         pass
#
# chelovek = Human(10)
# chelovek2 = Human(15)
# print(chelovek.height)
# print(Human.location)


# ЗАДАЧААА
import random
class Human:
    default_name = "Саня"
    default_age = "43"

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 69000
        self.__house = None

    def info(self):
        return self.name, self.age, self.__house, self.__money

    def earn_money(self):
        self.__money = self.__money + 25000

    def default_info(self):
        return Human.default_name, Human.default_age

    def __make_deal(self, dom):
        if self.__money >= dom.final_price(): # если хватает
            self.__money -= dom.final_price() # то тратим
            return True
        else:
            return False


    def buy_house(self, dom):
        if self.__make_deal(dom): # есди сделка успешна
            dom.owner = self.name # владелец дома
            self.__house = dom # владение дома
            return "Купили, сюда лут"
        else:
            return f"Денег не хватило, нужно еще {dom.final_price() - self.__money}"

class House:
    def __init__(self, adres = "Новосибирск, ул. Карла Либкнехта, д. 182", cena = 100000):
        self.__area = adres
        self.__price = cena
        self.skidka = random.randint(5, 25)

    def final_price(self):
        return self.__price - self.skidka / 100 * self.__price

chelovek = Human()
dom1 = House()
print(chelovek.buy_house(dom1))