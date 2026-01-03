from collections import defaultdict
s=[[0,1,2],[2,0,5]]
# score=defaultdict(int)
# for x,y,z in s:
#     score[x]-=z
#     score[y]+=z
# positives=[i for i in score.values() if i>0]
# negatives=[i for i in score.values() if i<0]
# def recurse(positives,negatives):
#     if len(positives)==0 and len(negatives)==0:
#         return 0
#     negative=negatives[0]
#     count=float("inf")
#     for positive in positives:
#         new_positive=positives.copy()
#         new_negative=negatives.copy()
#         new_positive.remove(positive)
#         new_negative.remove(negative)
#         if positive==-negative:
#             continue
#         elif positive>-negative:
#             new_positive.append(positive+negative)
#         else:
#             new_negative.append(positive+negative)
#     count=min(count,recurse(new_positive,new_negative))
#     return count+1
# print(recurse(positives,negatives))
scores=defaultdict(int)
for x,y,z in s:
    scores[x]-=z
    scores[y]+=z
positives=[i for i in scores.values() if i>0]
negatives=[i for i in scores.values() if i<0]
def dfs(positives,negatives):
    if len(positives)==0 and len(negatives)==0:
        return 0
    neg=negatives[0]
    co=float("inf")
    for pos in positives:
        new_positives=positives.copy()
        new_negatives=negatives.copy()
        new_positives.remove(pos)
        new_negatives.remove(neg)
        if pos==-neg:
            continue
        elif pos>-neg:
            new_positives.append(pos+neg)
        elif pos<-neg:
            new_negatives.append(pos+neg)
    co=min(co,dfs(new_positives,new_negatives))
    return co+1
print(dfs(positives,negatives))
    
