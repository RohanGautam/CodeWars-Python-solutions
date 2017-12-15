def diamond(n):
    if (n%2==0 or n<=0):return None
    L=['{}{}'.format(' '*((n-x)/2),'*'*x)for x in range(1,n+1,2) ]
    return '\n'.join(L)+'\n'+'\n'.join(L[::-1][1:])+'\n'