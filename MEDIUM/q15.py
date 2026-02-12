#Rearrange the array such that:

#Even index elements are smaller than next

#Odd index elements are greater than next
a=[3, 1, 2, 4]

largest=0
for i in range(0,len(a)-1):
    if i%2==0 and a[i]>a[i+1]:
        t=a[i]
        a[i]=a[i+1]
        a[i+1]=t
    if i%2!=0 and a[i]<a[i+1]:
        t=a[i]
        a[i]=a[i+1]
        a[i+1]=t


print(a)

