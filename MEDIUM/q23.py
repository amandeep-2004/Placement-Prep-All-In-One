a = [1,1,3,3,4,4,4,5,1,2]

d = {}
for x in a:
    d[x] = d.get(x, 0) + 1

pairs = []
for x in d:
    pairs.append((d[x], x))

# sort by frequency desc, value asc
pairs.sort(key=lambda p: (-p[0], p[1]))

res = []
for freq, val in pairs:
    res.extend([val] * freq)

print(res)
