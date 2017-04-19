import re
import itertools

def cleanup(L):
    returnL=[]
    for item in L:
        coeff= eval(re.sub('[a-zA-z]+','',item))
        if coeff>0:item='+'+item
        elif coeff<0:item=item
        else:item=''
        returnL.append(item)
    return returnL

def get_variable(x):
        return  re.sub(r'[-\+]\d*','',x)
    
def simplify(poly):    
    if poly[0] not in '-+':
        poly='+'+poly
    pattern1=re.compile(r'([-\+]{1}\w+)')    
    L=[''.join(sorted(x)) for x in pattern1.split(poly) if x<>'']
    L= sorted(L,key=get_variable)
    ordered=[ sorted(i) for i in sorted([list(g) for k,g in itertools.groupby(L,get_variable)])]
    mainlist=[]
    for alist in ordered:
        var=get_variable(alist[0])
        expression=''.join(alist)
        expression=re.sub(r'([-\+])([A-Za-z])',r'\1 1\2',expression)
        expression=re.sub(' ','',expression)
        expression=re.sub(var,'',expression)
        expression=str(eval(expression))+var
        mainlist.append(expression)
    mainlist=cleanup(mainlist)
    mainlist=sorted(mainlist,key=get_variable)
    ans=''.join(sorted(mainlist,key=len))
    ans=re.sub(r'([-\+])1',r'\1',ans)
    return ans.strip('+')
    
