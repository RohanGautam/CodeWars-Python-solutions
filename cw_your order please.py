import re
def fn(x):
    return int(re.findall('\d+',x)[0])

def order(s):
    words=s.split()
    return ' '.join(sorted(words,key=fn))
