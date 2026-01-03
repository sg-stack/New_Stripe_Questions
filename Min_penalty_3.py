
def get_closetime(l):
    closepenalty=0
    ind=-1
    currentpenalty=0
    for i in range(len(l)):
            if l[i]=="Y":
                currentpenalty-=1
            else:       
                currentpenalty+=1
            if currentpenalty<closepenalty:
                closepenalty=currentpenalty
                ind=i
    return ind+1

s=""
v=s.split(" ")
l=[]
q=""
m=[]
for i in range(len(v)):
    if v[i]=="BEGIN":
        m.append(v[i])
    elif v[i]=="END" and m[-1]=="BEGIN":
        l.append(q)
        q=""
        m.pop()
    else:
        if v[i].isalpha():
            q+=v[i]
if l:
    for u in range(len(l)):
        if l[u]:
            print("Closing time for log",l[u],"is at index:",get_closetime(l[u]))
        else:
            print("No valid logs found")
else:
    print("No valid logs found")



        