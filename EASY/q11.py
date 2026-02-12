#Find second largest distinct element in an array, or print “Not possible”.

a = [-100]

largest=float('-inf')
seclarge=float('-inf')
n=len(a)

for i in range(n):
    if a[i]>largest:
        seclarge=largest
        largest=a[i]
    elif a[i]>seclarge and a[i]!=largest:
        seclarge=a[i]

if seclarge==float('-inf'):
    print("not possible")
else:

    print("second largest element= ",seclarge)