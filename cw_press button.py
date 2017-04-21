#an alg that for some reason took me a lot of time to come up with.Enjoy!
def press_button(n):
    mcount,L=1,[]
    for number in range(n-1,0,-1):
        L.append(2*(mcount*number))
        mcount+=1
    till=((n-2)/2)
    L=L[:till]+[L[till]/2] if n%2==0 else L[:till+1]
    return sum(L)+n
