#Subarray with sum 0 exists or not (can have negative numbers).
a = [-1, 2, 3, -5, 1, 6, -6]

ps = 0
mp = {}

# prefix sum 0 before array starts
mp[0] = [-1]

for i, x in enumerate(a):
    ps += x

    if ps in mp:
        for prev in mp[ps]:
            print(a[prev + 1 : i + 1])
        mp[ps].append(i)
    else:
        mp[ps] = [i]
