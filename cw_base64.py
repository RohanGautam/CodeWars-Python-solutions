import string
seq=string.ascii_uppercase+string.ascii_lowercase+string.digits+'+/'
d1=dict(zip(range(64),seq))
d2=dict(zip(seq,range(64)))

def to_base_64(s):
    b=''.join(['{:08b}'.format(ord(letter)) for letter in s])
    bits=[b[i:i+6] for i in range(0,len(b),6)]
    b64=''
    for bit in bits:
        if len(bit)==6:
            b64+=d1[int(bit,2)]
        elif len(bit)==2:
            b64+=d1[int(bit+'0000',2)]
            b64+='=='
        elif len(bit)==4:
            b64+=d1[int(bit+'00',2)]
            b64+='='
    return b64.replace('=','')

def from_base_64(s):
    x=[d2[i] for i in s]
    x=['{:06b}'.format(i) for i in x]
    x=''.join(x)
    bits=[x[i:i+8] for i in range(0,len(x),8)]
    dec=[int(i,2) for i in bits]
    ascii=[chr(i) for i in dec]
    return  ''.join(ascii).replace('\x00', '')