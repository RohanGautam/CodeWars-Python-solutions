##Write a function that returns true or false depending on weather a number
##is prime or not

def is_prime(num):
    count=0
    num=abs(num)
    if num==0 or num==1:return False    
    for i in range(2,num-1):
        if num%i==0:count+=1
    
    if count==0:return True
    else:return False
