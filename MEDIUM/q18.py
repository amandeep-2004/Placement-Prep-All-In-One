#Two-sum variant: Given array and target, print all pairs (i, j) (indices or values) whose sum is target. Avoid duplicates.
a = [2, 8, 7, 3, 2, 5, 5, 1, 9]
target = 10
seen=set()
pair=set()


def cus_sort(x,z):
    if x>z:
        return (z,x)
    else:
        return (x,z)

for i in range(len(a)):
    y=target-a[i]
    if y in seen:
        j=a.index(y)
        pair.add(cus_sort(a[i],y))
        
    seen.add(a[i])

print(f"pair of elements:{list(pair)}")
