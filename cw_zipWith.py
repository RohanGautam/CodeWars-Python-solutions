def zip_with(fn,a1,a2):
    L=[]
    for x,y in zip(a1,a2):
        L.append(fn(x,y))
    return L
