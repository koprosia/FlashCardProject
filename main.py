from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#--DATA--#

data = pandas.read_csv("data/french_words.csv")
data_Frame = data.to_dict(orient="records")
random_record = ""


def create_english_image():
    global random_record
    canvas.itemconfig(logo_image, image=back_img)
    random_english_word = random_record["English"]
    canvas.itemconfig(card_text, text=random_english_word, fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.update()


def generate_word():
    global random_record, flip_timer
    window.after_cancel(flip_timer)
    random_record = random.choice(data_Frame)
    random_french_word = random_record["French"]
    canvas.itemconfig(card_text, text=random_french_word, fill = "black")
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(logo_image, image=logo_img)
    canvas.update()
    flip_timer = window.after(3000, create_english_image)

#---UI---#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(height=526, width=800)
flip_timer = window.after(3000, create_english_image)
#font image
logo_img = PhotoImage(file="images/card_front.png")
logo_image = canvas.create_image(400, 263, image=logo_img)

#back image
back_img = PhotoImage(file="images/card_back.png")

card_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"), tag="french text")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#Buttons
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=generate_word)
right_button.grid(row=1, column=0)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=1)

generate_word()

window.mainloop()

