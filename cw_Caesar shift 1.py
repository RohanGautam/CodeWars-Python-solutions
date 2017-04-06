##If the shift is initially 1, the first character of the message to be encoded will be shifted by 1,
##the second character will be shifted by 2, etc..
import string
from math import ceil
def splinto(s,n):
    L=[]  
    l_even=int(ceil((len(s)+0.0)/n))
    xo=range(l_even,len(s),l_even)
    for i in xo:
        L.append(s[i-l_even:i])
    L.append(s[xo[-1]:])
    while len(L)<>n:
        L.append('')
    return L

def moving_shift(s,shift):
    mstr=''
    x=s
    noreason1=string.ascii_lowercase*len(x)
    noreason2=string.ascii_uppercase*len(x)
    for i in x:
        if i.isalpha()==True:
            if i in string.ascii_lowercase:
                mstr+=noreason1[noreason1.index(i)+shift]
            else:
                mstr+=noreason2[noreason2.index(i)+shift]              
        else:
            mstr+=i
        shift+=1            
    return splinto(mstr,5)


print moving_shift("I should have known that you would have a perfect answer for me!!!", 1)
print 'Expected: ', ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]
##print string.ascii_lowercase[::-1]
def demoving_shift(arr,shift):
    mstr=''
    x=''.join(arr)
    noreason1=string.ascii_lowercase[::-1]*len(x)
    noreason2=string.ascii_uppercase[::-1]*len(x)
    for i in x:
        if i.isalpha()==True:
            if i in string.ascii_lowercase:
                mstr+=noreason1[noreason1.index(i)+shift]
            else:
                mstr+=noreason2[noreason2.index(i)+shift]
        else:
            mstr+=i
        shift+=1            
    return mstr
print demoving_shift(["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"],1)
