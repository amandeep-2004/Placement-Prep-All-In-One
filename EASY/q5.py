#converting a number to binary and hexadecimal

def toBinary(n):
    if n==0:
        print("0")
    a=[]
    idx=0   
    while(n>0):
        a.append(n%2)
        
        n=n//2
    print(a[::-1])

n=int(input("enter the number:"))
toBinary(n)
