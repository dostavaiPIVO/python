import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
total_bets = []
print(logo)
triger = "yes" # когда определять победителя
while triger == "yes":
    name = input("Имя: ")
    bet = int(input("ставка: "))
    temp_bet = {"name": name, "bet": bet}
    total_bets.append(temp_bet)

    triger = input("продолжаем? yes | | no")
    os.system("cls||clear")

winner = {'name': "", 'bet': 0}
for i in range(len(total_bets)):
    if total_bets[i]['bet'] > winner['bet']:
        winner['name'] = total_bets[i]['name']
        winner['bet'] = total_bets[i]['bet']
print(f"винер: {winner['name']} и его ставка: {winner['bet']}")


