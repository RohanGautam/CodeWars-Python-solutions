def solve(L):
    L=[''.join(sorted(list(set(x)))) for x in L]
    d=dict(zip(list(set(L)),eval('['+'[],'*len(list(set(L)))+']')))
    for ind,ele in enumerate(L):
        for x in d.keys():
            if ele==x:d[x].append(ind)
    return sorted([sum(x) for x in d.values() if len(x)>1])