##The maximum sum subarray problem consists in finding the maximum
##sum of a contiguous subsequence in an array or list of integers:
##
##maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
### should be 6: [4, -1, 2, 1]
##Easy case is when the list is made up of only
##positive numbers and the maximum sum is the sum of the whole array.
##If the list is made up of only negative numbers, return 0 instead.
##
##Empty list is considered to have zero greatest sum.
##Note that the empty list or array is also a valid sublist/subarray.


def maxSequence(arr):
    #return 0 if null list passed
    if arr==[]:return 0
    #return 0 if all elemnts are negative
    elif [0 for x in arr if x<0]==[0]*len(arr):return 0
    #return entire list's sum in all elements are positive
    elif [1 for x in arr if x>=0]==[1]*len(arr):return sum(arr)
    #else:
    else:
        maxsum=sum(arr)
        #finding the maximum contiguous sum
        for i in range(len(arr)):
            for j in range(len(arr)):
                if j>=i:
                    if sum(arr[i:j+1])>maxsum:
                        maxsum=sum(arr[i:j+1])
        return maxsum


#for example: this should return 6
print maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
