from itertools import *
import re
def unique_everseen(iterable, key=None):
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in ifilterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element
def proc_seq(*args):
    L=[list(chain(str(x))) for x in args]
    combos=list(set(list(product(*L))))
    numbers=[int(re.sub('^0\d+','0',''.join(x))) for x in combos]
    numbers=[x for x in numbers if x<>0]
    L=[len(numbers)]+list(unique_everseen([min(numbers),max(numbers),sum(numbers)]))
    return L
