#merging k sorted arrays

def merge_two(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    if i < len(a): res.extend(a[i:])
    if j < len(b): res.extend(b[j:])
    return res

def merge_k_sorted_divide_and_conquer(arrs: list[list[int]]) -> list[int]:
    if not arrs:
        return []
    # while more than one array, merge pairs
    while len(arrs) > 1:
        merged = []
        for i in range(0, len(arrs), 2):
            if i + 1 < len(arrs):
                merged.append(merge_two(arrs[i], arrs[i+1]))
            else:
                merged.append(arrs[i])
        arrs = merged
    return arrs[0]

# test
if __name__ == "__main__":
    k=int(input("enter the number of arrays:"))
    a=[]
    for i in range(k):
        print(f"enter the size of array {i+1}: ")
        n=int(input())
        if n==0:
            a.append([])
            continue
        print(f"enter the sorted elements of array {i+1}: ")
        arr=list(map(int,input().split()))
        a.append(arr)
    print(merge_k_sorted_divide_and_conquer(a))
