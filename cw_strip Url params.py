def strip_url_params(url, params_to_strip = []):
    if '?' not in url:return url
    url,que=url[:url.index('?')+1],url[url.index('?')+1:]
    que=que.split('&')
    L,ans=[],[]
    for x in que:
        if x[:x.index('=')] not in L and x[:x.index('=')] not in params_to_strip:
            L.append(x[:x.index('=')])
            ans.append(x)
    return url+'&'.join(ans)
