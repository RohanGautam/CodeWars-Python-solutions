def persistence(n):
    if len(str(n))==1:return 0
    n=eval('*'.join(str(n)))
    l=len(str(n))
    count=1    
    while l<>1:
        n=eval('*'.join(str(n)))
        l=len(str(n))
        count+=1
    return count
