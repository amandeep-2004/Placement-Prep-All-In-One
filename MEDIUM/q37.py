#Given an array of integers, return the k most frequent elements.
import heapq
a = [1,1,1,2,2,3,3,3,4]
k = 2

d = {}
for i in a:
    d[i] = d.get(i, 0) + 1

res = []
for i in d:
    res.append((i, d[i]))

res.sort(key=lambda x: (-x[1], x[0]))

ans = []
for i in range(k):
    ans.append(res[i][0])

print(ans)


def top_k_frequent(nums, k):
    freq = {}

    # count frequency
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    heap = []
    for val, f in freq.items():
        heapq.heappush(heap, (-f, val))

    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res