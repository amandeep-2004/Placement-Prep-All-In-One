#Remove all occurrences of pattern P from S (like repeatedly removing “ab” from a string).

s="abababcedab"
p="ab"

m=len(p)

stack=[]
for ch in s:
    stack.append(ch)
    if len(stack)>=m and ''.join(stack[-m:])==p:
        del stack[-m:]
print(''.join(stack))