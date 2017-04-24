import itertools
def permutations(string):
    return list(set([''.join(ele) for ele in itertools.permutations(string)]))
