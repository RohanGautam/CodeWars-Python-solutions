##In this kata you have to write a simple Morse code decoder.
##While the Morse code is now mostly superceded by voice and digital data
##communication channels,
##it still has its use in some applications around the world.

import re
def decodeMorse(morseCode):
    CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        ' ':'',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9':'----.'}
    CODE_REVERSED = {value:key for key,value in CODE.items()}
    finalstr=''
    for char in morseCode.split(' '):finalstr+= CODE_REVERSED[char]
    return re.sub('  ',' ',finalstr).strip(' ')
#for example:
print decodeMorse('.... . -.--   .--- ..- -.. .')

##this one got kinda tricky because one space was used between letters,
##and two between words as standard morse input
