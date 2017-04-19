import re
from itertools import groupby,chain
def mix(s1,s2):
    s1,s2=re.sub(r'[^a-z]+','',s1),re.sub(r'[^a-z]+','',s2)
    L1,L2=list(set(s1)),list(set(s2))
    uniqinL1,uniqinL2=[x for x in L1 if x not in L2],[x for x in L2 if x not in L1]
    d={}
    for x in L1:d[x]=(s1.count(x),s2.count(x))
    for x in uniqinL1:d[x]=(s1.count(x),0)
    for x in uniqinL2:d[x]=(0,s2.count(x))
    L=[]
    for key in sorted(d):
        if d[key][0]==d[key][1]:
            L.append(('=',d[key][0]))
            continue
        maxval=max(enumerate(d[key]),key=lambda x:x[1])
        L.append(maxval)
    main=[str(i[0])+':'+alphabet*i[1] for alphabet,i in zip(sorted(d),L)]
    main=[x for x in main if len(re.sub('[\d=]+:','',x))>1]
    main=[re.sub('1','2',x) for x in main]
    main=[re.sub('0','1',x) for x in main]
    main=sorted(main,key=len,reverse=True)
    Lax=[list(g) for k,g in groupby(main,key=len)]
    Lax=[sorted(x) for x in Lax]
    main=list(chain(*Lax))
    return '/'.join(main)

