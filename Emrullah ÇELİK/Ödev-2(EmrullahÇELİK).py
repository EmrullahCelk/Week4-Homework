import tkinter as tk
import string
import random


alphabets_big = list(set(list(string.ascii_letters.upper())))
alphabets_small = list(set(list(string.ascii_letters.lower())))
digits = list(string.digits)
special_characters = list(string.punctuation)
characters = alphabets_big + alphabets_small + digits + special_characters


def choice():
    lst = []

    for i in range(2):
        lst.append(random.choice(alphabets_big)) # 2 adet büyük harf
    for i in range(2):
        lst.append(random.choice(alphabets_small)) # 2 küçük harf
    for i in range(2):
        lst.append(random.choice(digits)) # 2 sayı seçimi
    for i in range(2):
        lst.append(random.choice(special_characters)) # 2 özel karakter seçimi
    for i in range(2):
        lst.append(random.choice(characters)) # diğer karakterlerden en az iki tane dediği için buraya tüm listeden random bir seçmi yaptırıyoruz

    password = []
    password = "".join(random.choice(lst) for i in range(10))
    print(password)
    label.config(text=password)


window = tk.Tk()

window.title("password")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="New password:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to choose a new password ", font="arial 12")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" Generation ", width=50, height=5, command=choice)
button1.grid(padx=110, pady=40)

window.mainloop()