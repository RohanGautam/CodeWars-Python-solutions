import copy
def diag_1_sym(s):
    w=[[x for x in ele]for ele in s.split('\n')]
    L,n=copy.deepcopy(w),len(w)
    for i in range(n):
        for j in range(n):
            L[i][j]=w[j][i]
    return '\n'.join([''.join(x) for x in L])
    
def rot_90_clock(strng):
    op=diag_1_sym(strng)
    return '\n'.join([x[::-1] for x in op.split('\n')])

def selfie_and_diag1(strng):
    op1,op2=strng.split('\n'),diag_1_sym(strng).split('\n')
    return '\n'.join([x+'|'+y for x,y in zip(op1,op2)])
def oper(fct, s):
    return fct(s)