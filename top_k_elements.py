freq=[[] for i in range(len(nums)+1)]
count={}
for i in nums:
    count[i]=count.get(i,0)+1
for n,c in count.items():
    freq[c].append(n)
res=[]
m=0
for u in range(len(freq)-1,-1,-1):
    if freq[u] and m<k:
        m+=len(freq[u])
        res.extend(freq[u])
return res