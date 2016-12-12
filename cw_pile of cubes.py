##Your task is to construct a building which will be a pile of n cubes.
##The cube at the bottom will have a volume of n^3,
##the cube above will have volume of (n-1)^3 and so
##on until the top which will have a volume of 1^3.
##
##You are given the total volume m of the building.
##Being given m can you find the number n of cubes you will have to build?
##
##The parameter of the function findNb (find_nb, find-nb)
##will be an integer m and you have to return the integer n such as
##n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or
##-1 if there is no such n.
import math

def find_nb(m):
    # (n(n+1)/2)^2 = m
    # n^2 + n - 2*sqrt(m) = 0
    # a = 1; b = 1; c = -2*sqrt(m)
    n = int(-1 + math.sqrt(1 + 8 * math.sqrt(m))) >> 1
     
    if ((n * (n + 1)) >> 1) ** 2 == m:
        return n
    return -1


#for testing purposes
#z=1071225        #would return 45
z=91716553919377 # would return -1
print find_nb(z)
