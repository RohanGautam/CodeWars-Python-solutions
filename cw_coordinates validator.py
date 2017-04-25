import re
def is_valid_coordinates(coordinates):
    L=[False]*2
    if coordinates.count(',')!=1:return False
    coords=[coord.strip() for coord in coordinates.split(',')]
    try:
        if -90<=eval(coords[0])<=90 and -180<=eval(coords[1])<=180:
            L=[re.sub(r'-?\d+\.?\d*','xrohanx',coord)=='xrohanx' for coord in coords ]
        return eval(' and '.join(map(str,L)))
    except:return False
