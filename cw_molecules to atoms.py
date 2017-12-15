import re

def unifybrackets(s):
    s=re.sub(r'[\[\{]','(',s)
    s=re.sub(r'[\]\}]',')',s)
    return s 

def getL(s):
    pattern=r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ][abcdefghijklmnopqrstuvwxyz]|[ABCDEFGHIJKLMNOPQRSTUVWXYZ]|\d+|[\(\)]'
    return re.findall(pattern,s)

def parse_molecule(formula):
    exp=unifybrackets(formula)
    Ls=getL(exp)
    L=[x for x in Ls if x.isalpha()]
    d=dict(zip(L,[0]*len(L)))
    L=Ls[:]
    for ind,ele in enumerate(Ls):
        if ele.isdigit():
            if L[ind-1].isalpha():
                L[ind-1]=(L[ind-1]+' ')*int(ele)
            elif L[ind-1]==')':
                substr='';i=ind-2
                while L[i]!='(':
                    substr+=L[i]
                    i-=1
                substr=' {} '.format(substr)
                L=L[:i]+['']*(ind-1-i)+[substr*int(ele)]+L[ind:]
    finalstr=' '.join(L)
    for key in sorted(d.keys(),key=len)[::-1]:
        d[key]=finalstr.count(key)
        finalstr=re.sub(key,'',finalstr)       
            
    return d