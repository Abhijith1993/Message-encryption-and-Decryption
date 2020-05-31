class Sele:
    def select_th(self):
        global seclect
        try:
            print('''What you Want To Do
            1. Encoding
            2. decoding''')
            seclect = int(input(">"))

            if seclect > 2 or seclect < 1:
                print("Please Enter Valid Value")
                Sele.select_th(self)
        except:
            print("Please Choose Any Value from option 1 OR 2 ")
            Sele.select_th(self)


class Mess:
    def message(self):
        global messages, words, length
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


class Fun:
    def function_n(self):
        onebyone = ""
        output = ""
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
        All_Function.here(self)


class All_Function:
    def here(self):
        Sele.select_th(self)
        Mess.message(self)
        Fun.function_n(self)


class main:
    All_Function.here(self=0)
