#string incrementer:
#Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number the number 1 should be appended to the new string.
#    Examples:
#foo -> foo1
#foobar23 -> foobar24
#foo0042 -> foo0043
#foo9 -> foo10
#foo099 -> foo100

import re
def increment_string(s):
    if not s: return '1'
    if s[-1] not in '0123456789':return s+'1'
    num=re.findall(r'\d+$',s)[0]
    word=re.sub(r'\d+$','',s)
    def get_num(n):
        zeroes=re.findall(r'^0+',n)
        zeroes=zeroes[0] if zeroes else ''
        num1=re.sub(r'^0+','',n)
        num1=num1 if num1 else '0'
        num2=str(int(num1)+1) 
        x=len(num2)-len(num1) if num2!='1' else 1
        return '0'*(len(zeroes)-x)+num2    
    return word+get_num(num)