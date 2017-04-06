def domain_name(s):
    if 'www' in s:
        x=s[s.index('.')+1:]
        x=x[:x.index('.')]
    else:
        x=s[s.index('/')+2:]
        x=x[:x.index('.')]
    return x

print domain_name("http://www.zombie-bites.com")
