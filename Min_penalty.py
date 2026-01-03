def func(log,close_time):
    penal=0
    for i in range(close_time):
        if log[i]=="N":
            penal+=1
    for i in range(close_time+1,len(log)):
        if log[i]=="Y":
            penal+=1
    return penal
print(func("NNNN",4))
