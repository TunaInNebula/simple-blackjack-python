# SIMPLE BLACKJACK GAME
from tkinter import *
import random

window = Tk()
window.title("Python Blackjack")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

label = Label(text="WELCOME TO BLACKJACK GAME")
label.config(bg="black")
label.config(fg="white")
label.pack()

user_card = 0
cpu_card = 0

user_card_list = []

cpu_card_list = []


def button_clicked():
    print("button clicked")



def game_start():
    # USER CARD LABEL
    your_card_label = Label(text="Kartlarınız") # your card label text
    your_card_label.config(bg="black")
    your_card_label.config(fg="white")
    your_card_label.pack(side=LEFT)
    # CPU CARD LABEL
    cpu_card_label = Label(text="Rakibinizin Kartları") # your card label text
    cpu_card_label.config(bg="black")
    cpu_card_label.config(fg="white")
    cpu_card_label.pack(side=RIGHT)



def cont_button_clicked():
    print("cont button clicked")  # button check
    user_card = random.randint(1,10) # users card config
    user_first_card = Label(text=f"{user_card}")
    user_first_card.config(bg="black")
    user_first_card.config(fg="white")
    user_first_card.pack(side=LEFT, padx=5)
    user_card_list.append(user_card)
    print(user_card_list)
    # CPU card
    cpu_card = random.randint(1,10) # cpu card config
    cpu_first_card = Label(text=f"{cpu_card}")
    cpu_first_card.config(bg="black")
    cpu_first_card.config(fg="white")
    cpu_first_card.pack(side=RIGHT, padx=5)
    cpu_card_list.append(cpu_card)
    print(cpu_card_list)


cont_button = Button(text="Kart Çek", command= cont_button_clicked)
cont_button.pack()

user_sum = sum(user_card_list)
cpu_sum = sum(cpu_card_list)

user_len = len(user_card_list)
cpu_len = len(cpu_card_list)


def game_end():
    if user_sum > 21 and user_len > 2:
        print("CPU kazandı")
    elif cpu_sum > 21 and cpu_len > 2:
        print("KAZANDINIZ")
    elif user_sum == 21:
        print("KAZANDINIZ")
    elif cpu_sum == 21:
        print("CPU kazndı")




game_start()
game_end()
window.mainloop()
