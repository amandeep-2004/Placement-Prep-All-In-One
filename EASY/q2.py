#palindrome

s=input("enter the string:")
l=len(s)
i=0
j=l-1
f=0
while i<l//2:
    if s[i]==s[j]:
        i+=1
        j-=1
        continue
    else:
        f=1
        break

if f==0:
    print("palindrome")
else:
    print("not palindrome")

