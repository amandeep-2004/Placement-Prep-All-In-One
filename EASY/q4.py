#Given an integer n, count number of set bits (1s in binary).

n=int(input("enter the number:"))
count=0
a=n
while n!=0:
    n=n&(n-1)
    count+=1
print("number of set bits in ",a,"=",count)