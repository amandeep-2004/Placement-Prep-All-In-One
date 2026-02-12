#Remove all occurrences of pattern P from S (like repeatedly removing “ab” from a string).
s = "abadababcde"
p = "ab"
m = len(p)

stack = []

for ch in s:
    stack.append(ch)

    if len(stack) >= m and ''.join(stack[-m:]) == p:
        del stack[-m:]

result = ''.join(stack)
print(result)
