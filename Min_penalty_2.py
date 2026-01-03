# Coding: Part-2
# co_y=customers.count("Y")
# co_n=0
# min_penalty=co_y
# ind=-1
# for i in range(len(customers)):
#     if customers[i]=="N":
#         co_n+=1
#     else:
#         co_y-=1
#     if co_n+co_y<min_penalty:
#         ind=i
#         min_penalty=co_n+co_y
# print(ind+1)

# optimized solution 

# closepenalty=0
# ind=-1
# currentpenalty=0
# for i in range(len(customers)):
#     if customers[i]=="Y":
#         currentpenalty-=1
#     else:       
#         currentpenalty+=1
#     if currentpenalty<closepenalty:
#         closepenalty=currentpenalty
#         ind=i+1
# print(ind)