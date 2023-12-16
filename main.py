# SIMPLE BLACKJACK GAME

from tkinter import *
import tkinter
import random

window = Tk()
window.title("Python Blackjack")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

label = Label(text="WELCOME TO BLACKJACK GAME")
label.config(bg="black")
label.config(fg="white")
label.pack()


def button_clicked():
    print("button clicked")


button = Button(text="ENTER", command=button_clicked)

button.pack()

user_score = 0
cpu_score = 0


# user_label = Label(text=f"{user_score}")
# print("welcome to blackjack game")

# print("lütfen başlamak için ENTER'a basın")

def game_start():
    user_score = random.randint(0, 21)
    print(f"kartınız {user_score}")
    user_label = Label(text=f"kartınız {user_score}")
    user_label.config(bg="black")
    user_label.config(fg="white")
    user_label.pack()
    cpu_score = random.randint(0, 21)
    cpu_label = Label(text=f"rakibinizin kartı {cpu_score}")
    cpu_label.config(bg="black")
    cpu_label.config(fg="white")
    cpu_label.pack()
    print(f"bilgisayarın kartı {cpu_score}")


game_start()
window.mainloop()
