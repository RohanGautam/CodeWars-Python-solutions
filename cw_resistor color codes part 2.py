import re
d={0: 'black', 1: 'brown', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'blue', 7: 'violet', 8: 'gray', 9: 'white'}
def encode_resistor_colors(ohmstr):
    ohm=re.sub(' ohms','',ohmstr)
    if ohm[-1]=='k':ohm='{:g}'.format(eval(re.sub('k','',ohm))*1000)
    if ohm[-1]=='M':ohm='{:g}'.format(eval(re.sub('M','',ohm))*1000000)
    colors=[d[int(i)] for i in ohm[:2]]
    colors.append(d[ohm[2:].count('0')])    
    colors.append('gold')
    return ' '.join(colors)
