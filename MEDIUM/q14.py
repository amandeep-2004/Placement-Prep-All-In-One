#kadane's algorithm to find subarray with max sum

a=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
bl=-1
br=-1
curmax=a[0]
gmax=a[0]
curstart=0

for i in range(1,len(a)):
    x=a[i]
    if x>curmax+x:
        curmax=x
        curstart=i
    else:
        curmax=curmax+x
    if curmax>gmax:
        gmax=curmax
        bl=curstart
        br=i

print(f"subarray:{a[bl:br+1]}\nmax sum:{gmax}\nlength of array:{br-bl+1}")