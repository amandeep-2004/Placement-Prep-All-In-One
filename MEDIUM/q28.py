#GCD of array of n numbers.

a=[]
n=int(input("enter the number of elements in array: "))
for i in range(n):
    a.append(int(input()))

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
g=a[0]
for i in range(len(a)):
    g=gcd(g,a[i])
    
print(f"GCD of {a} = {g}")