print('''What you Want To Do
1. Encoding
2. decoding'''  )
seclect = int(input(">"))
messages = input(">")
words = messages.split()
length = len(messages)




encode = {
    "a": "{",
    "b": "|",
    "c": "}",
    "d": "~",
    "e": "ÿ",
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
"ÿ": "e",
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
onebyone =""
output =""
for i in range(length):
    onebyone += messages[i]
if seclect == 1:
    for word in onebyone:
        output += encode.get(word, word) + " "
    print(output)
elif seclect == 2:
    for word in onebyone:
        output += decoding.get(word, word) + " "
    print(output)
else:
    print(" Enter 1 or 2 only")





