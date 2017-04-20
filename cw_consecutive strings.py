def longest_consec(strarr,k):
    if strarr==[] or k<=0 or k>len(strarr):return '' 
    L=[''.join(strarr[i:i+k]) for i in range(len(strarr)-(k-1))]
    maax=L[0]
    for i in L:
        if len(i)>len(maax):maax=i
    return maax
