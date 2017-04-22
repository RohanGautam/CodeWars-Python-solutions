def rotate_paper(number):
    if number=='1':return False
    n=''
    for i in number:
        if i=='6':n='9'+n
        if i=='9':n='6'+n
        if i in '12508':n=i+n
    return n==number
        
