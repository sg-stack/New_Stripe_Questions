adj=defaultdict(list)
for x,y in relations:
    adj[x].append(y)
max_time={}
def dfs(src):
    if src in max_time:
        return max_time[src]
    res=time[src-1]
    for x in adj[src]:
        res=max(res,time[src-1]+dfs(x))
    max_time[src]=res
    return res
for u in range(1,n+1):
    dfs(u)
return max(max_time.values())