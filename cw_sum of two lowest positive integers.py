##Create a function that returns the sum of the two lowest positive
##numbers given an array of minimum 4 integers.
##No floats or empty arrays will be passed.
##For example,
##when an array is passed like [19,5,42,2,77], the output should be 7.
##Do not modify the original array
def sum_two_smallest_numbers(numbers):
    number=numbers #lol
    number.sort(reverse=True)
    a=number.pop()
    b=number.pop()
    return a+b

print sum_two_smallest_numbers([4,3,2,1])
