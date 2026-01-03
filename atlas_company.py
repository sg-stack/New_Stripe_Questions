# import re
# Suff= {"inc.", "corp.", "llc", "l.l.c.", "llc."}
# Lead_art= {"the", "an", "a"}
# def normalize(comp_name):
#     if not comp_name:
#         return
#     comp_name=comp_name.lower()
#     comp_name=comp_name.replace("&"," ").replace(","," ")
#     comp_name=re.sub(r"/s+"," ",comp_name)
#     for i in Suff:
#         if comp_name.endswith(" "+i):
#             comp_name=comp_name[:-len(i)].strip()
#         elif comp_name==i:
#             comp_name=" "
#     words=comp_name.split()
#     if words and words[0] in Lead_art:
#         words=words[1:]
#     res=""
#     for i,num in enumerate(words):
#         if num=="And" and i!=0:
#             continue
#         res+=num
#     return res
# def validate_company_name(expression):
#     for x,y in expression:
#         validate_name=normalize(y)
#         if not validate_name:
#             print(f"{x}| Name Not Available ")
#         elif validate_name in reg_names:
#             print(f"{x} | Name Not Available")
#         else:
#             print(f"{x}|{validate_name} Name is Available")
#             reg_names[validate_name]=x
# def reclaim(li):

#     for x,y in li:
#         val_name=normalize(y)
#         if reg_names[val_name]==x:
#             del reg_names[val_name]
#             print("successfully reclaimed",reg_names)
#         else:
#             print("Access denied to your account")
# reg_names={}
# vali=[["12345","Lllama Inc."],["34abc","Intel corp."],["5678io","lllama corp."]]
# v=validate_company_name(vali)
# print(reclaim([["12345","Lllama Inc."],["34abc","Intel corp."]]))

# Card Range Obfuscation
# x=input()
# n=int(input())
# track="0"
# for i in range(n):
#     ran1,ran2,ran3=map(str,input().split(","))
#     if len(x)==16:
#         print(x)
#         break
#     else:
#         sp1=x+track+"0"*10
#         sp2=x+ran2
#         track=str(int(ran2[0])+1)
#         print(sp1+","+sp2+","+ran3)

bin_val = input().strip()
n = int(input().strip())

intervals = []
for _ in range(n):
    line = input().split(',')
    intervals.append((int(line[0]), int(line[1]), line[2]))

intervals.sort()

current_pos = 0
max_val = 9999999999

for i in range(len(intervals)):
    start_off, end_off, brand = intervals[i]
    
    # Check for a gap before this interval
    if start_off > current_pos:
        # Fill gap using the current interval's brand
        gap_start = f"{bin_val}{current_pos:010d}"
        gap_end = f"{bin_val}{start_off - 1:010d}"
        print(f"{gap_start},{gap_end},{brand}")
    
    # Print the interval itself
    out_start = f"{bin_val}{start_off:010d}"
    out_end = f"{bin_val}{end_off:010d}"
    print(f"{out_start},{out_end},{brand}")
    
    current_pos = end_off + 1

# Check for a gap at the very end
if current_pos <= max_val:
    last_brand = intervals[-1][2]
    out_start = f"{bin_val}{current_pos:010d}"
    out_end = f"{bin_val}{max_val:010d}"
    print(f"{out_start},{out_end},{last_brand}")