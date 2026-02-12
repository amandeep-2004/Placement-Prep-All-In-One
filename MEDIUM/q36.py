#Given N, generate all balanced parentheses of length 2N.
def validpar(n,p):
    res=[]
    def backtrack(curr,open,close):
        if len(curr)==2*n:
            res.append(curr)
            return
        if open<n:
            backtrack(curr+p[0],open+1,close)
        if close<open:
            backtrack(curr+p[1],open,close+1)
    backtrack("",0,0)
    return res
n=int(input("enter the Number of valid paranthesis to generate: "))
p=input("enter the open parenthesis and close parenthesis: (){}[]")
print(validpar(n,p))
