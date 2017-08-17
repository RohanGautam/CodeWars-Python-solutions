def solution(n):
    L=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sym=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    d=dict(zip(L,sym))
    ans=''
    while n!=0:
        highest_roman_dec=max([num for num in L if n/num!=0])
        n-=highest_roman_dec
        ans+=d[highest_roman_dec]
    return ans