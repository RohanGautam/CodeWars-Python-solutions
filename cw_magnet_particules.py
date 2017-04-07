from __future__ import division
def doubles(maxk, maxn):
    sum=0
    for k in range(1,maxk+1):
        for n in range(1,maxn+1):
            sum+=1/(k*((n+1)**(2*k)))
    return sum
