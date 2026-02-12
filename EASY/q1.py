#Given an array, print the index of first and last occurrence of a target. If not found, print -1 -1.

a=[1,2,3,5,1,4,6,1]
t=int(input("enter the target: "))
st=-1 #set starting occurence as -1
ei=-1 #ending occurance as -1
l=len(a)
i=0
while(i<l):
    if a[i]==t: #if the element is target element
        if st==-1: #then check whether its first occurance or not
            st=i
        ei=i
    i+=1

print("index of first occurence of target= ",st)
print("index of last occurence of target= ",ei)
    