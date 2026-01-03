def dfs(curr_exp):
    closed_bracket=curr_exp.find("}")
    if closed_bracket==-1:
        res.add(curr_exp)
        return
    open_bracket=curr_exp.rfind("{",0,closed_bracket-1)
    prefix=curr_exp[:open_bracket]
    suffix=curr_exp[closed_bracket+1:]
    content=curr_exp[open_bracket+1:closed_bracket]
    for x in content.split(","):
        dfs(prefix+x+suffix)
res=set()
dfs(expression)
res=list(res)
res=sorted(res)
return res