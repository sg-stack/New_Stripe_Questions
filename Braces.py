s=" hello-}-weird-{-world"
sta=s.find("{")-1
end=s.find("}")+1
sta1=s.find("{")
end1=s.find("}")
b=s[sta+2:end-1]
b=b.split(",")
if sta1<end1 and sta1>=0 and end1>=0 and len(b)>1:
    q=""
    for r in b:
        q+=s[:sta+1]
        q+=r
        q+=s[end:]
        print('"'+q+'"')
        q=""
else:
    print(s)
    "Hello"
    "good thing"
    "very very good github tutorial done"