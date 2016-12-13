##A Narcissistic Number is a number which is the sum of its own digits,
##each raised to the power of the number of digits.
##
##For example, take 153 (3 digits):
##
##    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153



def nar(x):
    su=0
    x=str(x)
    for i in range(len(x)):
        su+=pow(int(x[i]),len(x))
    if su==int(x):return True
    else:return False

#for example
print nar(371)
