##Build Tower by the following given argument:
##number of floors (integer and always greater than 0).
##Tower block is represented as *
##In Python, return a list.
##a tower of 6 floors looks like below
##
##[
##  '     *     ', 
##  '    ***    ', 
##  '   *****   ', 
##  '  *******  ', 
##  ' ********* ', 
##  '***********'
##]


def tower_builder(n):
    L=[]
    for i in range(1,n+1):
        L.append(' '*(n-i)+'*'*(i+(i-1))+' '*(n-i))
    return L



