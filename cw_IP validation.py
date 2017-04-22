import re
def is_valid_IP(strng):
    L=re.findall(r'(\d+)\.?',strng)
    if len(L)<>4:return False
    s2=strng.replace('.','')
    if re.sub('\d+','#',s2)<>'#':return False
    return [True for snum in L if 0<=int(snum)<=255 and snum[0]<>'0']==[True]*4
