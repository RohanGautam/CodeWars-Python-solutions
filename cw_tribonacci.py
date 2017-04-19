def tribonacci(signature,n):
    if n==0:return []
    if len(signature)>n:return [signature[0]]
    while len(signature)<>n:
        signature.append(sum(signature[-3:-1]+[signature[-1]]))
    return signatures
