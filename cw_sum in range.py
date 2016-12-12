##Given two integers, which can be positive and negative,
##find the sum of all the numbers between including them too
##and return it. If both numbers are equal return a or b.
##
##Note! a and b are not ordered!


def get_sum(a,b):
    L=[]
    if a>b: L=[x for x in range(b,a+1)]
    elif a<b: L=[x for x in range(a,b+1)]
    else: return a
    return sum(L)

#for example
print get_sum(1,1)
