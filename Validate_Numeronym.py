def validNumeronym(word,abbr):
    i,j=0,0
    while i<len(word) and j<len(abbr):
        if abbr[j].isalpha():
            if word[i]!=abbr[j]:
                return False
            i+=1
            j+=1
        else:
            if abbr[j]=="0":
                return False
            num=0
            while j<len(abbr) and abbr[j].isdigit():
                num=num*10+int(abbr[j])
                j+=1
            i+=num
    return True

print(validNumeronym("internationalization", "i18n"))  # True
print(validNumeronym("apple", "a3e"))                  # True
print(validNumeronym("apple", "a2e"))                  # False
print(validNumeronym("apple", "a01e"))                 # False
