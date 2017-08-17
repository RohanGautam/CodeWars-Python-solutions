def find_missing(L):
    x=[L[i+1]-L[i] for i in range(len(L)-1)]
    d=x[0] if x.count(x[0])!=1 else x[1]
    l=list(set(x))
    ele=l[0] if x.count(l[0])==1 else l[1]
    pos=x.index(ele)
    return L[pos]+d