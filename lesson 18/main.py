import easygui

# user_choose = easygui.msgbox(
#     msg="Hello world!",
#     title="Усиленно приветствую",
#     ok_button="есть!",
#     image="imagess/maska.png"
# )
#
# if user_choose == None:
#     easygui.msgbox(msg="Ну пока")
# elif user_choose == "есть!":
#     print("ы")




# easygui.buttonbox(
#     msg="гоу?",
#     title="заголовок",
#     choices=("play dota", "я не гей"),
#     images=["imagess/лол.png", "imagess/1.png"]
# )



# x = easygui.integerbox(
#     msg="сколько игр на наге?",
#     upperbound= 150, # верхняя граница
#     lowerbound= 50,   # нижняя граница
#     image="imagess/comp.png"
# )
# print(x)


name = easygui.enterbox(
    msg="ну шо ти? тебя как звать псина?",
    default="Данил"
)
print(name)