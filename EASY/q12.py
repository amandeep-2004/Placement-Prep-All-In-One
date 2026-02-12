#Frequency of each element in an array, print element + count (no inbuilt Counter / fancy libs).

d={}
a=[1,2,1,1,3,2,4,3]
for i in a:
    d[i]=d.get(i,0)+1
for i in d:
    print("frequency of ",i,"=",d[i])

#max frequency
mf=0
mfi=0
for i in d:
    if d[i]>mf:
        mf=d[i]
        mfi=i
print("element with max frequency:\n element= ",mfi,"\nfrequency= ",mf)