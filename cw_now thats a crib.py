def my_crib(floors):
    maxwidth=(floors*5)+(floors-1)+2
    house=['{:^{maxwidth}}'.format('_'*(floors*2+1),maxwidth=maxwidth)]
    house.extend(['{:^{maxwidth}}'.format('/{}\\'.format('_'*(i)),maxwidth=maxwidth) for i in range(floors*2+1,((floors*5)+(floors-1)+1),2)])
    house.extend(['|{}|'.format(' '*(maxwidth-2)) for _ in range(floors-1)])
    house.append('|{:^{maxwidth}}|'.format('_'*(floors*2-1),maxwidth=maxwidth-2))
    house.extend(['|{:^{maxwidth}}|'.format('|{}|'.format(' '*(floors*2-1)),maxwidth=maxwidth-2) for _ in range(floors-1)])
    house.append('|{:_^{maxwidth}}|'.format('|{}|'.format('_'*(floors*2-1)),maxwidth=maxwidth-2))
    return  '\n'.join(house)
