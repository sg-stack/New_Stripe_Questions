# Problem
# import bisect
# from collections import defaultdict
# text = "The quick brown fox is quick and very quick fox"
# query = "quick fox"
# query=query.split(" ")
# k = 2
# def pre_process(text):
#     text=text.lower().split()
#     for i in range(len(text)):
#         adj[text[i]].append(i)
# adj=defaultdict(list)
# words=pre_process(text)
# def result(query,adj):
#     for u in adj[query[0]]:
#         sta=u
#         fo=True
#         for j in query[1:]:
#             pos=adj[j]
#             idx=bisect.bisect_right(pos,sta)
#             if idx==len(pos) or pos[idx]-sta>k:
#                 fo=False
#                 break
#             sta=idx
#         if fo:
#             res.append(u)
#     return res

# res=[]
# print(result(query,adj))
