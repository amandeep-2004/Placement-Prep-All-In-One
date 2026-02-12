#Group anagrams: given list of words, group them as list of anagram groups

#method 1
a=["eat", "tea", "tan", "ate", "nat", "bat"]
d={}
for i in a:
    key=''.join(sorted(i))
    if key not in d:
        d[key]=[]
    d[key].append(i)
    
print(list(d.values()))

#method 2
c={}
for i in a:
    f=[0]*26
    for j in i:
        f[ord(j)-ord('a')]+=1
    key=tuple(f)
    if key not in d:
        c[key]=[]
    c[key].append(i)
    
print(list(c.values()))