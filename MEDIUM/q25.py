a = [1, 8, 2, 3, 4, 1]
n = len(a)
res = [-1] * n
stack = []

for i in range(n):
    while stack and a[i] > a[stack[-1]]:
        
        idx = stack.pop()
        res[idx] = a[i]
    stack.append(i)
print(res)