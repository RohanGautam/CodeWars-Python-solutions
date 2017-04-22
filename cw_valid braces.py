#input=> a combination of (,){,},[,]
def validBraces(braces):
    d,L,stack,braces={'}':'{',']':'[',')':'('},[],[],list(braces)
    try:
        for brace in braces:
            if brace in '{[(':
                stack.append(brace)
            else:
                L.append(stack.pop()==d[brace])
        return eval(' and '.join(map(str,L)))
    except:return False
