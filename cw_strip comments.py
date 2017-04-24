import re
def solution(string,markers):
    lines=string.split('\n')
    lines=[(re.sub('['+'|'.join(markers)+'].+','',line)).strip() if re.search('['+'|'.join(markers)+']',line) <>None else line for line in lines ]
    return '\n'.join(lines)
