from player import MusicBox

player = MusicBox()
while True:
    player.play()
    guess = input("что ты услышал? ")
    if guess == "":
        break
    player.check(guess)
print(f"очков:", {player.get_score()})