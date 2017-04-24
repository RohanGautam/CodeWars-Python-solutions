def next_bigger(n):
    c=n
    if len(str(n))==1:return -1
    if str(n)==''.join(sorted(str(n),reverse=True)):return -1
    if len(str(n))==2:return int(str(n)[::-1])
    while True:
        c+=1
        if sorted(str(c))==sorted(str(n)) and c>n:
            return c
