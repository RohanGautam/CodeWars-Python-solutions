def remove(s):
    s=list(s)
    if s!=[]:
        if s[len(s)-1]=='!':s.pop()
    return ''.join(s)

print remove('')
