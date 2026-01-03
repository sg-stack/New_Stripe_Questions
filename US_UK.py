# def build(inp):
#     graph={}
#     for i in inp.split(":"):
#         src,dest,way,co=i.split(",")
#         graph.setdefault(src,{})[dest]=int(co)
#     return graph
# def direct_cost_graph(inp,src,dest):
#     x=build(inp)
#     return x.setdefault(src,{}).get(dest,-1)
# def one_stop_graph(inp,src,dest):
#     x=build(inp)
#     mi_co=float("inf")
#     for i in x[src]:
#         print(i)
#         if i in x and dest in x[i]:
#             mi_co=min(mi_co,x[src][i]+x[i][dest])
#     return mi_co
# s="US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7"
# print(direct_cost_graph(s,"US","UK"))
# print(one_stop_graph(s,"US","UK"))
# from collections import defaultdict
# import heapq
# adj=defaultdict(list)
# n = 5
# m= 6
# edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
# for x,y,z in edges:
#     adj[x].append([y,z])
# cos=[float("inf")]*(n+1)
# parent=list(range(n+1))
# cos[1]=0
# pq=[(0,1)]
# while pq:
#     dist,node=heapq.heappop(pq)
#     for adjnode,adjcos in adj[node]:
#         if dist+adjcos<cos[adjnode]:
#             cos[adjnode]=dist+adjcos
#             heapq.heappush(pq,(cos[adjnode],adjnode))
#             parent[adjnode]=node
# path=[]
# node=n
# while parent[node]!=node:
#     path.append(node)
#     node=parent[node]
# path.append(1)
# path.reverse()
# print(path)
import heapq
from collections import defaultdict

def main():
    n = int(input("enter the entries: "))

    # graph[source] = [(cost, destination), ...]
    graph = defaultdict(list)

    for _ in range(n):
        source = input("source: ")
        destination = input("destination: ")
        product = input("Product: ")   # read but not used (same as your C++ code)
        cost = int(input("cost: "))

        graph[source].append((cost, destination))

    s = input("give the source: ")
    d = input("give the destination: ")

    # Min-heap priority queue
    pq = []
    heapq.heappush(pq, (0, s))

    INF = float("inf")
    dist = defaultdict(lambda: INF)
    dist[s] = 0

    while pq:
        curr_cost, node = heapq.heappop(pq)

        # Skip outdated entries
        if curr_cost > dist[node]:
            continue

        # Early exit if destination reached
        if node == d:
            break

        for edge_cost, next_node in graph[node]:
            new_cost = curr_cost + edge_cost

            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    if dist[d] == INF:
        print(-1)
    else:
        print(dist[d])


if __name__ == "__main__":
    main()
