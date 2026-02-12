def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

L = int(input())
R = int(input())
A = int(input())
b = int(input())

countA = R//A - (L-1)//A
countb = R//b - (L-1)//b

lcm = A*b // gcd(A,b)
countboth = R//lcm - (L-1)//lcm

print("div count:", countA + countb - countboth)
