#Remove duplicates from a sorted array in-place, return length of unique segment.
a=[1,2,3,4,4,5,6,7]
n=0
print("before removing duplicates:")
print(a)
print("length of array: ",len(a))
for i in range(1,len(a)-1):
    if a[i]!=a[n]:
        n+=1
        a[n]=a[i]
print("after removing duplicates:")
print(a[:n+1])
print("length of array: ",n+1)
