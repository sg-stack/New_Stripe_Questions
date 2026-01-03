adj=defaultdict(list)
for x,y,z in flights:
    adj[x].append([y,z])
dist=[float("inf")]*(n)
e=deque()
dist[src]=0
e.append((0,src,0))
while e:
    stops,node,dis=e.popleft()
    if stops>k:
        break
    for adjnode,cost in adj[node]:
        if dis+cost<dist[adjnode]:
            dist[adjnode]=dis+cost
            e.append((stops+1,adjnode,dist[adjnode]))
if dist[dst]==float("inf"):
    return -1
else:
    return dist[dst]