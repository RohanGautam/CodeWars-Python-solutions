import textwrap
def align_right(text,width):    
    if len(text)<=width:return '{:>{width}}'.format(text,width=width)
    lines=textwrap.wrap(text,width)
    lines=['{:>{width}}'.format(line.strip(),width=width) for line in lines]
    return '\n'.join(lines)
