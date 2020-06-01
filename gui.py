import tkinter
from tkinter import scrolledtext
from tkinter import *



encode = {
    "a": "{",
    "b": "|",
    "c": "}",
    "d": "~",
    "e": "",
    "f": "Ç",
    "g": "ü",
    "h": "é",
    "I": "â",
    "j": "ä",
    "k": "à",
    "l": "å",
    "m": "ç",
    "n": "ê",
    "o": "ë",
    "p": "è",
    "q": "ï",
    "r": "î",
    "s": "ì",
    "t": "æ",
    "u": "Æ",
    "v": "ô",
    "w": "ö",
    "x": "ò",
    "y": "û",
    "z": "ù",
    "A": "®",
    "B": "¯",
    "C": "³",
    "D": "´",
    "E": "¸",
    "F": "¹",
    "G": "¾",
    "H": "À",
    "I": "Á",
    "J": "Â",
    "K": "Ã",
    "L": "Ä",
    "M": "Å",
    "N": "È",
    "O": "É",
    "P": "Ê",
    "Q": "Ë",
    "R": "Ì",
    "S": "Í",
    "T": "Î",
    "U": "Ï",
    "V": "Ð",
    "W": "Ò",
    "X": "Ó",
    "Y": "Ô",
    "Z": "Õ",

}
decoding = {
    "{": "a",
    "|": "b",
    "}": "c",
    "~": "d",
    "": "e",
    "Ç": "f",
    "ü": "g",
    "é": "h",
    "â": "I",
    "ä": "j",
    "à": "k",
    "å": "l",
    "ç": "m",
    "ê": "n",
    "ë": "o",
    "è": "p",
    "ï": "q",
    "î": "r",
    "ì": "s",
    "æ": "t",
    "Æ": "u",
    "ô": "v",
    "ö": "w",
    "ò": "x",
    "û": "y",
    "ù": "z",
    "®": "A",
    "¯": "B",
    "³": "C",
    "´": "D",
    "¸": "E",
    "¹": "F",
    "¾": "G",
    "À": "H",
    "Á": "I",
    "Â": "J",
    "Ã": "K",
    "Ä": "L",
    "Å": "M",
    "È": "N",
    "É": "O",
    "Ê": "P",
    "Ë": "Q",
    "Ì": "R",
    "Í": "S",
    "Î": "T",
    "Ï": "U",
    "Ð": "V",
    "Ò": "W",
    "Ó": "X",
    "Ô": "Y",
    "Õ": "Z",

}

window = Tk()

window.title("E.D Message", )
window.geometry('500x500')

lbl = Label(window, text="Enter or Paste Your Text", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

txt = scrolledtext.ScrolledText(window, width=60, height=10)
txt.grid(column=0, row=1)


lbl = Label(window, text="OutPut", font=("Arial Bold", 12))
lbl.grid(column=0, row=5)

out = scrolledtext.ScrolledText(window, width=60, height=10)
out.grid(column=0, row=6)



def clicked(): #----------take data -----------------
    input_tx = txt.get("1.0", 'end-1c')
    input_tx +=" hello"

    #--------show dataa----------------
    out.insert("1.0", input_tx)




btn = Button(window, text="Encode", width=70, height=3, font=("Arial Bold", 8), command=clicked)
btn.grid(column=0, row=3)


btn1 = Button(window, text="Decode", width=70, height=3, font=("Arial Bold", 8), command=clicked)
btn1.grid(column=0, row=4)

window.mainloop()

# ----------------------tker Funtiofon------------------------------------
message = txt.get()
