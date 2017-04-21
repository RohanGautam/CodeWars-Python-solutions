#algorithm i came up with after a lot of messing around, should've
#taken me a looot lesser time lol XD
def sum_them(n):
    if n==0:return 0
    n=(2<<(n-1))    #faster way to do 2**n, because we're using bit shifting.2**n would still work though
    return (n*(n+1))/2
