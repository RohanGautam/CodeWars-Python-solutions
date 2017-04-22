def mult_triangle(n):
    total_sum=((n*(n+1))/2)**2
    total_even_sum=(((n*(n+1))/2)-(n+1)/2)**2
    total_odd_sum=total_sum-total_even_sum
    return [total_sum,total_even_sum,total_odd_sum]
