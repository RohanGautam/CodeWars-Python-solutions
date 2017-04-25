def move_zeros(array):
    return sorted(array,key=lambda x:not bool(x) and (str(x).isdigit() or type(x)==float))
