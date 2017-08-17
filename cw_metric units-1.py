import re
L=[int('1'+'0'*i) for i in [0,3,6,9,12,15,18,21,24]]
sym='m km Mm Gm Tm Pm Em Zm Ym'.split()
d=dict(zip(L,sym))
def fn(n):
    n=eval(re.sub(r'\.0+$|0+$','',str(n)))
    return n
def meters(n):
    h=max([num for num in L if n/num>=1]) 
    x=float(n)/h
    return "{}".format(fn(x))+d[h]