from классы import Human, House
import easygui

imya = easygui.enterbox(msg="Как твоё имя?")
age = easygui.integerbox(msg="Сколько тебе лет?")
price_house = easygui.integerbox(msg="Цена дома", upperbound=1000000000 )
adres = easygui.enterbox(msg="Адрес твоей халупи")

chelovek = Human(imya, age)
dom1 = House(adres, price_house)

print(chelovek.buy_house(dom1))



