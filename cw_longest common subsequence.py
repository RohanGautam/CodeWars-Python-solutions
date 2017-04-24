import itertools
def lcs(x, y):
    x=''.join([i for i in x if i in y])
    subseq=[]
    for i in range(1,len(y)+1):
        subseq.extend([''.join(ele) for ele in list(itertools.combinations(y,i))])
    substr,L=[],[]
    for i in range(1,len(x)+1):
        substr.extend([''.join(ele) for ele in list(itertools.combinations(x,i))])
    L=[ele for ele in substr if ele in subseq]
    return sorted(L,key=len)[-1] if bool(L) else ''
