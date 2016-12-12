##Implement the function unique_in_order which takes as
##argument a sequence and returns a list of items without any
##elements with the same value next to each other and preserving
##the original order of elements.
##
##For example:
##    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
##    unique_in_order([1,2,2,3,3])       == [1,2,3]
def unique_in_order(iterable):
    #converting iterable to list and adding null str so that seperator logic works
    st=list(iterable)+['']
    L=[]
    for i in range(len(st)-1):  
        if st[i]<>st[i+1]:
            L.append(st[i])
    return L
#for example:(this would work for strings as well)
print unique_in_order([1,2,2,3])
