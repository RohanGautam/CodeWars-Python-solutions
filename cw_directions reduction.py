import re
def dirReduc(arr):
    s=' '.join(arr)
    p1,p2=re.compile('NORTH SOUTH'),re.compile('SOUTH NORTH')
    p3,p4=re.compile('EAST WEST'),re.compile('WEST EAST')
    for i in range(8):
        s=' '.join(s.split())
        s=p1.sub('',s)
        s=p2.sub('',s)
        s=p3.sub('',s)
        s=p4.sub('',s)
    return s.split()
