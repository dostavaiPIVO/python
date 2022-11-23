import random
import datetime

while True:
    number = input("Сколько др мы генерируем (до 70)?")
    if not number.isdigit() or int(number) > 70 or int(number) < 2:
        print("число от 2 до 70, идиот")
        print("-" * 8)
    else: # если все гудентак
        number = int(number) # строчка --> число
        break # выход из while True

birthdays = []
startofyear = datetime.date(2022, 1, 1)
for _ in range(number):
    shift = random.randint(0, 364)
    shiftofdays = datetime.timedelta(shift)
    birthday = startofyear + shiftofdays
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays[index]}")

print("-" * 10)
for i in set(birthdays): # множество, повторения исключены
    if birthdays.count(i) > 1: # два и более повторения
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза.") 

