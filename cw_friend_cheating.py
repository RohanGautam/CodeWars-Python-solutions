##A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
##Within that sequence, he chooses two numbers, a and b.
##He says that the product of a and b should be equal to the sum
##of all numbers in the sequence, excluding a and b.
##Given a number n, could you tell me the numbers he excluded
##from the sequence?
##The function takes the parameter:
##n (don't worry, n is always strictly greater than 0 and small
##enough so we shouldn't have overflow) and returns an array of the form:
##
##[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
##with all (a, b)which are the possible removed numbers in the
##sequence 1 to n.
##unfortunately, this works for small numbers as i couldnt figure out a more efficient way, and codewars wouldnt accept my solution :/


def removNb(n):
    L=range(1,n+1)
    L2=[]
    for a in range(len(L)):
        for b in range(len(L)):            
            sumL=sum([x for x in L if x!=L[a] and x!=L[b]])            
            if L[a]*L[b]==sumL:
                L2.append(tuple([L[a],L[b]]))

    return L2

print removNb(26)
