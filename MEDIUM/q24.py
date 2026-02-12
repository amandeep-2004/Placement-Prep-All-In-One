#String compression: "aaabbcccc" → "a3b2c4". If compressed bigger than original, return original.

s="aaabbcccc"
res=[]
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        res.append(s[i-1]+str(c))
        c=1
res.append(s[-1]+str(c))

snew=''.join(res)
if len(snew)<len(s):
    print(snew)
else:
    print(s)
