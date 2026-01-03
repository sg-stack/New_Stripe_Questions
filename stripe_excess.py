s="aeiouaeiou"
m=0
vow="aeiou"
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         v=s[i:j+1]
#         if len(v)>=5:
#             res=all(ch in v for ch in p)
#             if res:
#                 m+=1
# print(m)
    
# def checkvow(freq):
#     return (freq.get('a',0)>=1 and freq.get('e',0)>=1 and freq.get('i',0)>=1 and freq.get('o',0)>=1 and freq.get('u',0)>=1)
# vow="aeiou"
# co=0
# for i in range(len(s)):
#     if s[i] not in vow:
#         continue
#     freq={}
#     sta=i
#     while sta<len(s) and s[sta] in vow:
#         freq[s[sta]]=freq.get(s[sta],0)+1
#         if checkvow(freq):
#             co+=1
#         sta+=1
# print(co)
las={v:-1 for v in vow}
n=len(s)
sta=0
for i in range(n):
    if s[i] not in vow:
        las={v:-1 for v in vow}
        sta=i+1
        continue
    las[s[i]]=i
    if -1 not in las.values():
        print(las)
        m+=min(las.values())-sta+1
print(m)

