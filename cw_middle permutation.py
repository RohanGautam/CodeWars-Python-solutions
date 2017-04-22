def middle_permutation(s):
    string=sorted(s)
    n=len(string)/2 if len(string)%2==0 else (len(string)/2)+1
    begin=string[n-1] if len(string)%2==0 else string[n-1]+string[string.index(string[n-1])-1]
    ans=begin+''.join([x for x in string if x not in begin][::-1])
    return ans
