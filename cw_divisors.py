##Create a function named divisors that takes an integer
##and returns an array with all of the integer's
##divisors(except for 1 and the number itself).
##If the number is prime return the string'(integer) is prime'
##example:
##    divisors(12); #should return [2,3,4,6]
##    divisors(25); #should return [5]
##    divisors(13); #should return "13 is prime"

def divisors(integer):
    L=[]
    count=0
    for i in range(2,int(integer/2)+1):
        if integer % i==0:
            L.append(i)
            count+=1
    if count != 0:return L
    else:return str(integer)+' is prime'
