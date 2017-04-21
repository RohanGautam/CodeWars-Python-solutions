def sel_reverse(arr,l):
    print  arr,l
    if l==0:return arr
    if l>=len(arr):return arr[::-1]
    L=[]
    r=range(l,len(arr),l)
    for i in r:
        L.extend(list(reversed(arr[i-l:i])))
    print L
    L.extend(list(reversed(arr[r[-1]:])))
    return L
    
        
    
        
