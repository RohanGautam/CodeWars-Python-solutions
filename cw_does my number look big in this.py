def narcissistic( value ):
    return sum([int(x)**len(str(value)) for x in str(value)])==value
