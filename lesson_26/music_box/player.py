from random import choice
import playsound

class MusicBox:
    def __init__(self):
        self.__variants = "abdegv"
        self.__score = 0
        self.__sequence = choice(self.__variants)

    def get_score(self):
        return self.__score

    def play(self):
        for bukva in self.__sequence:
            playsound.playsound(f"sounds/{bukva}.mp3")

    def check(self, guess:str):
        if guess.lower().strip() == self.__sequence:
            playsound.playsound("sounds/win.mp3")
            self.__score += 1
            self.__next()
        else:
            playsound.playsound("sounds/lose.mp3")
            self.__score -= 0.5

    def __next(self):
        #self.__sequence += choice(self.__variants) # 1 вариант (кал) просто добалвяем к букве прежней
        __dlinna = len(self.__sequence) + 1 # генерим заново всё
        self.__sequence = ""
        for _ in range(__dlinna):
            self.__sequence += choice(self.__variants)
