##Given two arrays a and b write a function comp(a, b)
##that checks whether the two arrays have the "same" elements,
##with the same multiplicities. "Same" means, here,
##that the elements in b are the elements in a squared,
##regardless of the order.
##Example:
##  a = [121, 144, 19, 161, 19, 144, 19, 11]  
##  b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
##      comp(a,b) would return True here.

import math
def comp(array1, array2):    
    if array1!=None and array2!=None:
        if len(array1)==len(array2):
            array1=list(set(array1))
            array2=list(set(array2))
            array2=[math.sqrt(x)for x in array2]
            array1.sort();array2.sort()
    return array1==array2          

#for example
print comp([1,2,3],[1,4,9])
                    
