def my_crib(floors):
    maxwidth=(floors*2)+2
    house=['{:^{maxwidth}}'.format('/{}\\'.format(' '*(i*2)),maxwidth=maxwidth) for i in range(floors)]
    house.append('/{}\\'.format('_'*(floors*2)))
    house.extend(['|{}|'.format(' '*(floors*2)) for _ in range(floors-1)])
    house.append('|{}|'.format('_'*(floors*2)))
    return '\n'.join(house)
