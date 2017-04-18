def decode_resistor_colors(bands):
    bands+=' x'
    bands=bands.split()
    d={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'gray':8,'white':9}
    tolerance={'gold':5,'silver':10,}
    resistance=eval(''.join([str(d[x]) for x in bands[:2]]))
    resistance=resistance*(10**d[bands[2]])
    if resistance>=1000000:resistance='{:g}'.format(resistance/1000000.0)+'M'
    elif resistance>=1000:resistance='{:g}'.format(resistance/1000.0)+'k'  
    return "{} ohms, {tol}%".format(resistance,tol=tolerance.get(bands[3],20))
