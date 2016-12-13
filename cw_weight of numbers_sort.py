##My friend John and I are members of the "Fat to Fit Club (FFC)".
##John is worried because each month a list with the weights
##of members is published and each month he is the last on the
##list which means he is the heaviest.
##
##I am the one who establishes the list so I told him:
##    "Don't worry any more, I will modify the order of the list".
##It was decided to attribute a "weight" to numbers.
##The weight of a number will be from now on the sum of its digits.
##
##For example 99 will have "weight" 18, 100 will have
##"weight" 1 so in the list 100 will come before 99.
##Given a string with the weights of FFC members in normal
##order can you give this string ordered by "weights" of these numbers?
##When two numbers have the same "weight", let us class them
##as if they were strings and not numbers: 100 is before 180
##because its "weight" (1) is less than the one of 180 (9) and
##180 is before 90 since, having the same "weight" (9) it comes
##before as a string.

def order_weight(s):
    s=s.split()
    L=[]
    #making a list with the sum of digits of each number
    for i in range(len(s)):
        sx=0
        for x in s[i]:
            sx+=int(x)
        L.append(sx)
        
    s=map(int,s)#mapping every element of s to an integer
    #A bit of bubble sortin' :
    for i in range(len(L)-1,0,-1):#to sort according to int comparison:
        for j in range(i):
            if L[j]>L[j+1]:                
                L[j+1],L[j]=L[j],L[j+1]
                s[j+1],s[j]=s[j],s[j+1]
    #to sort according to str comparison, if adjacent values are equal:
    #this is bad, but i did the below steps three times for more accuracy.one is enough though
    for i in range(len(L)-1):
        if L[i]==L[i+1]:            
            if str(s[i])>str(s[i+1]):
              L[i+1],L[i]=L[i],L[i+1]
              s[i+1],s[i]=s[i],s[i+1]

    for i in range(len(L)-1):
        if L[i]==L[i+1]:            
            if str(s[i])>str(s[i+1]):
              L[i+1],L[i]=L[i],L[i+1]
              s[i+1],s[i]=s[i],s[i+1]
              
    for i in range(len(L)-1):
        if L[i]==L[i+1]:            
            if str(s[i])>str(s[i+1]):
              L[i+1],L[i]=L[i],L[i+1]
              s[i+1],s[i]=s[i],s[i+1]
    for i in range(len(L)-1):
        if L[i]==L[i+1]:            
            if str(s[i])>str(s[i+1]):
              L[i+1],L[i]=L[i],L[i+1]
              s[i+1],s[i]=s[i],s[i+1]
    for i in range(len(L)-1):
        if L[i]==L[i+1]:            
            if str(s[i])>str(s[i+1]):
              L[i+1],L[i]=L[i],L[i+1]
              s[i+1],s[i]=s[i],s[i+1]
    for i in range(len(L)-1):
        if L[i]==L[i+1]:            
            if str(s[i])>str(s[i+1]):
              L[i+1],L[i]=L[i],L[i+1]
              s[i+1],s[i]=s[i],s[i+1]
    
    return ' '.join(map(str,s))   
    
    
print order_weight('1 2 200 4 4 6 6 7 7 27 72 18 81 9 91 425 31064 7920 67407 96488 34608557 71899703')

