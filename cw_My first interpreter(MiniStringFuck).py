def miniStringFuck(code):
    memory_cell=0
    answerfuck=''
    for instruction in code:
        if instruction =='+':
            if memory_cell==255:memory_cell=0
            else:memory_cell+=1
        if instruction=='.':
            answerfuck+=chr(memory_cell)
    return answerfuck
            
            
