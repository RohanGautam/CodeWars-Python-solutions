def find_even_index(arr):
    for index in range(len(arr)):
        L1,L2=arr[:index],arr[index+1:]
        if sum(L1)==sum(L2):
            return index
    return -1
