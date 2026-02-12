#Remove all the occurences of the target element from the array( in place)
a=[1,2,3,3,4]
target=3
k=0
for i in range(len(a)):
    if target!=a[i]:
        
        a[k]=a[i]
        k+=1
print(a[:k])