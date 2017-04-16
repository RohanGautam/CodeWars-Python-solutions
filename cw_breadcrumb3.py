import re
def generate_bc(url,seperator=' '):
    url=re.split('/+',url)
    if url[0]=='http:':del(url[0])
    if url[0]=='https:':del(url[0])
    if '' in url:del(url[url.index('')])
    url[0]='HOME'
    if len(url)==1:return '<span class="active">{}</span>'.format(re.sub('-',' ',url[0]).upper())        
    if url[-1][:5]=='index':del(url[-1])
    url[-1]=re.sub(r'\..+','',url[-1])
    url[-1]=re.sub(r'\?.+','',url[-1])
    url[-1]=re.sub(r'#.+','',url[-1])
    if len(url)==1:return '<span class="active">{}</span>'.format(re.sub('-',' ',url[0]).upper())
    bc0=[]
    for i in range(1,len(url[1:])+1):
        bc0.append(url[i])
        if len(url[i])>30:            
            word=''.join([x[0] for x in url[i].split('-') if x not in ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]])
            url[i]=word
        elif '-' in url[i]:
            url[i]=re.sub('-',' ',url[i])
    urlink,L=[],[]
    for i in bc0:
        L.append(i)
        urlink.append('/'.join(L))    
    bc=['<a href="/">{}</a>'.format(url[0].upper())]
    bc.extend(['<a href="/{}/">{}</a>'.format(urlink[i-1],url[i].upper()) for i in range(1,len(url)-1)])    
    bc.append('<span class="active">{}</span>'.format(re.sub('-',' ',url[-1]).upper()))
    return seperator.join(bc)
