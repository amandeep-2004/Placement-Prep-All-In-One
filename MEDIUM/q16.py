#Given an array, find minimum positive integer that cannot be formed as sum of subset.

a = [1, 1, 3, 4, 9,6,7]
a.sort()
sum=0

for i in a:
    if i>sum+1:
        print(f"minimum sum:{sum+1}")
        break
    else:
        sum+=i


print(f"minimum sum:{sum+1}")