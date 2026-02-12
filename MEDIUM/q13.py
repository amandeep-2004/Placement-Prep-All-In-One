#Smallest subarray with sum ≥ K. Given array of positive integers & K, find minimum length of subarray whose sum ≥ K. If none, print 0.

def subarray(arr,k):
    if k<=0:
        return 1 if arr else 0
    left=0
    cur_sum=0
    n=len(arr)
    min_len=n+1
    bl=-1
    br=-1
    for right in range(n):
        cur_sum+=arr[right]
        while cur_sum>=k:
            if right-left+1<min_len:
                min_len=right-left+1
                bl=left
                br=right
            cur_sum-=arr[left]
            left+=1
    if bl==-1:
        print("no valid array")
    else:
        print("subarray: ",arr[bl:br+1])
        print("lenggth of subarray= ",br-bl+1)


a = [2, 3, 1, 2, 4, 3]
k = 7
subarray(a,k)