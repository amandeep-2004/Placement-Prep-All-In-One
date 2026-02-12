#Check if a string is valid bracket sequence: ()[]{} etc, using stack.
s="[()]}"
def validbracket(s):
    stack=[]
    m={')':'(',']':'[','}':'{'}
    for i in range(len(s)):
        if s[i] in m.values():
            stack.append(s[i])
        elif s[i] in m:
            if not stack or stack[-1]!=m[s[i]]:
                return False
            stack.pop()
    return len(stack)==0

p=validbracket(s)

if p==True:
    print("valid")
else:
    print("invalid")