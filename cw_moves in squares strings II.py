def rot(strng):
    return '\n'.join([x[::-1] for x in strng.split('\n')][::-1])
def selfie_and_rot(strng):
    dots='.'*len(strng.split('\n')[0])
    return '\n'.join([x+dots for x in strng.split('\n')]+[dots+x[::-1] for x in strng.split('\n')][::-1])
def oper(fct, s):
    return fct(s)
