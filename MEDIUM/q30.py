#Given N intervals, merge all overlapping intervals.

a = [[1, 4], [2, 5], [3, 6]]
a.sort(key=lambda x:x[0])

merged = [a[0]]

for i in range(1, len(a)):
    last = merged[-1]

    if a[i][0] <= last[1]:
        last[1] = max(last[1], a[i][1])
    else:
        merged.append(a[i])
total=0
for i in range(len(merged)):
    total+=merged[i][1]-merged[i][0]

print(total)
