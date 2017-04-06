

def is_valid(coords):
    L=[]
    x=[i.strip()for i in coordinates.split(',')]
    #for first coordinate:
    fc=x[0]
    try:
        if abs(int(fc[:2])) in range(0,91):
            if '.' in fc:
                a=int(fc[3:])
            L.append(True)
    except:
        L.append(False)
    #for second coordinate:
    sc=x[1]:
    scl=sc.split('.')
    try:
        if abs(int(scl[0])) in range(0,181):
            if '.' in sc:
                a=int(scl[1])
            L.append(True)
    except:
        L.append(False)

    if L=[True]*2:
        return True
    else:
        return False
