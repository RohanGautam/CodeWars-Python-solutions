def diag_2_sym(s):
    return '\n'.join([''.join(x) for x in zip(*s.split('\n'))])[::-1]
def rot_90_counter(s):
    return '\n'.join([''.join(x)[::-1] for x in zip(*s.split('\n'))])[::-1]  
def selfie_diag2_counterclock(s):
    return '\n'.join([x+'|'+y+'|'+z for x,y,z in zip(s.split('\n'),diag_2_sym(s).split('\n'),rot_90_counter(s).split('\n'))])
def oper(fct, s):
    return fct(s)

#if s='abcd\nefgh\nijkl\nmnop'
#then to transpose it in a lit way:
#zip(*s.split('\n'))