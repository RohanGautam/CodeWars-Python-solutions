##John and Mary want to travel between a few towns A, B, C ...
##Mary has on a sheet of paper a list of distances between these towns.
##ls = [50, 55, 57, 58, 60].
##John is tired of driving and he says to Mary that he doesn't
##want to drive more than t = 174 miles and he will visit only 3 towns.
##
##Which distances, hence which towns, they will choose so that
##the sum of the distances is the biggest possible - to please Mary -
##but less than t - to please John- ?

##t-max distance
##k- number of towns
##ls-list of distances
import itertools
def choose_best_sum(t,k,ls):
    combos=list(itertools.combinations(ls,k))
    sums=[sum(i) for i in combos]
    sums2=[i for i in sums if i<=t]#only the sums we care about
    if sums2==[]:
        largest=None
    else:
        largest=max([i for i in sums if i<=t])
    return largest

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]    
print choose_best_sum(430,8,xs)
