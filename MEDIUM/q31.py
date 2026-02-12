#Minimum platforms required for trains, given arrival & departure times.
a=[900,940,950,1100,1500,1800]
d=[910,1200,1120,1130,1900,2000]
a.sort()
d.sort()
i=j=0
p=0
mp=0

while i<len(a) and j<len(d):
    if a[i]<=d[j]:
        p+=1
        mp=max(mp,p)
        i+=1
    else:
        p-=1
        j+=1
print(mp)