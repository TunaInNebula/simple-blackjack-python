# SIMPLE BLACKJACK GAME
from tkinter import *
import random
from tkinter import messagebox

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
    user_first_card.config(bg="green")
    user_first_card.config(fg="white")
    user_first_card.pack(side=LEFT, padx=5)
    user_card_list.append(user_card)
    print(user_card_list)

    # Güncellenen user_sum
    global user_sum
    user_sum = sum(user_card_list)
    user_score_label.config(text=f"Toplam: {user_sum}")

    # CPU card
    cpu_card = random.randint(1,10) # cpu card config
    cpu_first_card = Label(text=f"{cpu_card}")
    cpu_first_card.config(bg="purple")
    cpu_first_card.config(fg="white")
    cpu_first_card.pack(side=RIGHT, padx=5)
    cpu_card_list.append(cpu_card)
    print(cpu_card_list)

    # güncellenen cpu sum

    global cpu_sum
    cpu_sum = sum(cpu_card_list)
    cpu_score_label.config(text=f"Toplam: {cpu_sum}")



    #oyun sonu

    game_end()




cont_button = Button(text="Kart Çek", command= cont_button_clicked)
cont_button.pack()


def stop_button_clicked():
    print("stop button clicked")
    global cpu_sum

    if cpu_sum < 21 and cpu_sum < user_sum:
        print("pass")
        cpu_card = random.randint(1, 10)  # cpu card config
        cpu_first_card = Label(text=f"{cpu_card}")
        cpu_first_card.config(bg="black")
        cpu_first_card.config(fg="white")
        cpu_first_card.pack(side=RIGHT, padx=5)
        cpu_card_list.append(cpu_card)
        print(cpu_card_list)

        cpu_sum = sum(cpu_card_list)
        cpu_score_label.config(text=f"Toplam: {cpu_sum}")


    if user_sum > cpu_sum:
        print("KAZANDINIZ")
        messagebox.showinfo(title="Decrypted Text", message="KAZANDINIZ")

    elif cpu_sum > user_sum:
        print("CPU kazandı")
        messagebox.showinfo(title="Decrypted Text", message="CPU KAZANDI")

    else:
        print("BERABERE")
        messagebox.showinfo(title="Decrypted Text", message="BERABERE")

    game_end()





stop_button = Button(text="Dur", command= stop_button_clicked)
stop_button.pack()

user_sum = sum(user_card_list)
cpu_sum = sum(cpu_card_list)

user_score_label = Label(text=f"toplam: {user_sum}")
user_score_label.pack(side=LEFT, pady=15)

cpu_score_label = Label(text=f"toplam: {cpu_sum}")
cpu_score_label.pack(side=RIGHT, pady=15)


def game_end():
    print(f"user_sum:{user_sum} ")
    print(f"cpu sum: {cpu_sum} ")
    if user_sum > 21 >= cpu_sum:
        print("CPU kazandı")
        messagebox.showinfo(title="Decrypted Text", message="CPU KAZANDI")

    elif cpu_sum > 21 >= user_sum:
        print("KAZANDINIZ")  # hatırlatma messagebox kullan
        messagebox.showinfo(title="Decrypted Text", message="KAZANDINIZ")

    elif user_sum == 21 and cpu_sum != 21:
        print("KAZANDINIZ")
        messagebox.showinfo(title="Decrypted Text", message="KAZANDINIZ")

    elif cpu_sum == 21 and user_sum != 21:
        print("CPU kazandı")
        messagebox.showinfo(title="Decrypted Text", message="CPU KAZANDI")

    elif user_sum > 21 and cpu_sum > 21:
        print("BERABERE")
        messagebox.showinfo(title="Decrypted Text", message="BERABERE")



# ...

def restart_game():

    for widget in window.winfo_children():
        if isinstance(widget, Label):
            user_score_label.destroy()
    # Temizleme işlemleri
    user_card_list.clear()
    cpu_card_list.clear()
    user_sum = 0
    cpu_sum = 0

    # Metinleri güncelle
    user_score_label.config(text=f"Toplam: {user_sum}")
    cpu_score_label.config(text=f"Toplam: {cpu_sum}")

    # ...
    game_start()

# ...

restart_button = Button(text="Yeniden Başlat", command=restart_game)
restart_button.pack()

# ...




game_start()


window.mainloop()
