import string
s=string.ascii_lowercase
S=string.ascii_uppercase
def rot13(message):
    d,d2=dict(zip(s[:13],s[13:])),dict(zip(s[13:],s[:13]))
    D,D2=dict(zip(S[:13],S[13:])),dict(zip(S[13:],S[:13]))
    d.update(d2),D.update(D2)
    encoded=''
    for letter in message:
        if letter.islower():encoded+=d[letter]
        elif letter.isupper():encoded+=D[letter]
        else:encoded+=letter
    return encoded