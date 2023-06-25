# Created by Emma Hodor

import tkinter
import pandas
import os

BACKGROUND_COLOR = "#B1DDC6"
picked = []
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR, height=1000, width=1000)


def swap_english():
    flashcard.itemconfig(image_used, image=flash_back)
    flashcard.itemconfig(language, fill="white", text="English")
    flashcard.itemconfig(word, text=picked["ENGLISH"], fill="white")

swap = window.after(ms=3000, func=swap_english)

def new_word_wrong():
    global picked, swap
    window.after_cancel(swap)
    picked = spanish.sample()
    picked = picked.squeeze()
    flashcard.itemconfig(word, text=picked['SPANISH'], fill="black")
    flashcard.itemconfig(image_used, image=flash_front)
    flashcard.itemconfig(language, fill="black", text="Spanish")
    swap = window.after(ms=3000, func=swap_english)

def new_word_correct():
    global picked, swap
    for dict in spanish_dict:
        if picked["SPANISH"] in dict.values():
            spanish_dict.remove(dict)
        df = pandas.DataFrame(spanish_dict)
        df.to_csv("to_learn.csv", index=False)
    window.after_cancel(swap)
    picked = spanish.sample()
    picked = picked.squeeze()
    flashcard.itemconfig(word, text=picked['SPANISH'], fill="black")
    flashcard.itemconfig(image_used, image=flash_front)
    flashcard.itemconfig(language, fill="black", text="Spanish")
    swap = window.after(ms=3000, func=swap_english)

flashcard = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard.place(x=65, y=0)
flash_front = tkinter.PhotoImage(
    file="/Users/emmahodor/PycharmProjects/100DayPython/FlashCardApp/images/card_front.png")
flash_back = tkinter.PhotoImage(file="/Users/emmahodor/PycharmProjects/100DayPython/FlashCardApp/images/card_back.png")
image_used = flashcard.create_image(400, 270, image=flash_front)

language = flashcard.create_text(390, 150, text="Spanish", font=("Arial", 50, "italic"))

x = tkinter.PhotoImage(file="/Users/emmahodor/PycharmProjects/100DayPython/FlashCardApp/images/wrong.png")
x_button = tkinter.Button(image=x, command=new_word_wrong)
x_button.place(x=250, y=550)
x_button.config(highlightbackground=BACKGROUND_COLOR, highlightthickness=0, background=BACKGROUND_COLOR)

cor = tkinter.PhotoImage(file="/Users/emmahodor/PycharmProjects/100DayPython/FlashCardApp/images/right.png")
cor_button = tkinter.Button(image=cor, command=new_word_correct)
cor_button.place(x=570, y=550)
cor_button.config(highlightbackground=BACKGROUND_COLOR)

word = flashcard.create_text(390, 300, text="word", font=("Arial", 70, "bold"))

if os.path.isfile("to_learn.csv"):
    spanish = pandas.read_csv("to_learn.csv")
else:
    spanish = pandas.read_csv("spanishflash.csv")
spanish_dict = spanish.to_dict(orient="records")
print(spanish_dict)
new_word_wrong()
swap = window.after(ms=3000, func=swap_english)

window.mainloop()
