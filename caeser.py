def alphabet_position(letter):
    ##Usage: Returns a int for the letters space in the alphabet.
    #a returns 0,b returns 1,z returns 25
    alphalist = ("abcdefghijklmnopqrstuvwxyz")

    if type(letter) == str and letter.isalpha() == True:
        if letter.lower() in alphalist:
            return alphalist.index(letter.lower())
    else:
        return alphalist[int(letter)]
def rotate_character(char, rot):
    #returns a,1 as b,returns c,2 as e
    uppercase = 0
    if char.isalpha() == True:
        if char.isupper() == True:
            uppercase += 1
        intchar = alphabet_position(char)
        intchar = (intchar + rot) % 26
        intchar = alphabet_position(intchar)

        if uppercase == 0:
            return intchar
        else:
            return intchar.upper()
    else:
        return char

def encrypt(text, rot):
    newtext = []
    for i in text:
        newtext.append(rotate_character(i,rot))
    newtext = "".join(newtext)

    return newtext        
