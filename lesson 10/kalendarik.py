import datetime

MONTHS =("январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь")
DAYS = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "восресенье")

while True:
    year = input("Год: ")
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break

while True:
    month = input("Месяц: ")
    if month.isdigit() and int(month) > 0:
        month = int(month)
        break

calText = ""
calText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"

for i in range(7):
    calText += DAYS[i] + " "

print(calText)
weekSeparator = ("+----------" * 7) + "\n"
blankRow = ("          " * 7) + "|\n"


