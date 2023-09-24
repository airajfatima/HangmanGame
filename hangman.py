from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as tmsg
from string import ascii_uppercase
import random


window = Tk()
window.title('Hangman - GUESS COUNTRY NAME')
label = Label(text="GUESS THE COUNTRY", font=(
    'consolas 28 bold')).grid(row=0, column=1, columnspan=6, padx=10)
word_list = ['CHINA', 'ITALY', 'FRANCE', 'SPAIN', 'TURKEY', 'GERMANY', 'MALAYSIA', 'CANADA', 'GREECE', 'THAILAND', 'MEXICO',
             'MOROCCO', 'JAPAN', 'INDIA', 'BRAZIL', 'NORWAY', 'SWEDAN', 'NEPAL', 'RUSSIA']

photos = [PhotoImage(file="Hangman/images/hang0.png"), PhotoImage(file="Hangman/images/hang1.png"), PhotoImage(file="Hangman/images/hang2.png"),
          PhotoImage(file="Hangman/images/hang3.png"), PhotoImage(
              file="Hangman/images/hang4.png"), PhotoImage(file="Hangman/images/hang5.png"),
          PhotoImage(file="Hangman/images/hang6.png"), PhotoImage(
              file="Hangman/images/hang7.png"), PhotoImage(file="Hangman/images/hang8.png"),
          PhotoImage(file="Hangman/images/hang9.png"), PhotoImage(file="Hangman/images/hang10.png"), PhotoImage(file="Hangman/images/hang11.png")]


def newGame():
    global word_space
    global Guesses
    Guesses = 0

    the_word = random.choice(word_list)
    word_space = " ".join(the_word)
    Word_dash.set(' '.join("_"*len(the_word)))
    imgL.config(image=photos[0])


def guess(letter):
    global Guesses
    if Guesses < 11:
        txt = list(word_space)
        guessed = list(Word_dash.get())
        if word_space.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                Word_dash.set("".join(guessed))
                if Word_dash.get() == word_space:
                    x = tmsg.askquestion(
                        "Hangman", "You guessed it!\nDo you want to start a new game?")
                    if x == "yes":
                        newGame()
                        break
                    else:
                        exit()

        else:
            Guesses += 1
            imgL.config(image=photos[Guesses])
            if Guesses == 11:
                Word_dash.set(' '.join(word_space))
                x = tmsg.askquestion(
                    "Hangman", "Game Over!\nDo you want to start a new game?")
                if x == "yes":
                    newGame()
                else:
                    exit()


# images
imgL = Label(window)
imgL.grid(row=2, column=2, columnspan=3, padx=10, pady=40)

# word
Word_dash = StringVar()
Label(window, textvariable=Word_dash, font=('consolas 24 bold')).grid(
    row=1, column=1, columnspan=6, padx=10)

# keyboard
n = 0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=(
        'Helvetica 18 bold'), width=4).grid(row=3+n//9, column=n % 9)
    n += 1
Button(window, text="NEW\nGAME", command=lambda: newGame(),
       font=("Helvetica 12 bold"), width=6).grid(row=5, column=8)

newGame()
window.mainloop()
