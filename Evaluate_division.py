equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
from collections import defaultdict
adj=defaultdict(list)
for i,eq in enumerate(equations):
    a,b=eq
    adj[a].append([b,values[i]])
    adj[b].append([a,1.0/values[i]])
def dfs(start,target,curr_val,vis):
    if start in vis or target in vis or start not in adj or target not in adj:
        return -1
    if start==target:
        return 1
    vis.add(start)
    for node,weight in adj[start]:
        res=dfs(node,target,curr_val*weight,vis)
        if res!=-1:
            return res
    return res
[dfs(q[0],q[1],1,set()) for q in queries]

