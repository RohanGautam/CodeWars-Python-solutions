def missing_alphabets(s):
    soln=[]
    s=''.join(sorted(s))
    print s
    setalpha=max([s.count(x) for x in list(set(s))])
    print setalpha
    for x in list('abcdefghijklmnopqrstuvwxyz'):
        if x*setalpha not in s:
            if x not in s:soln.append(x*setalpha)
            else:soln.append(x*(setalpha-s.count(x)))            
    return ''.join(sorted(soln))
