#Longest substring without repeating characters.

s=input("enter the string: ")
last={}

left=0
bl=0
blen=0
br=0

for right,ch in enumerate(s):
    if ch in last and last[ch]>=left:
        left=last[ch]+1
    last[ch]=right
    curlen=right-left+1
    if curlen>blen:
        blen=curlen
        bl=left
        br=right
print(f"longest substring without repeating characters: {s[bl:br+1]}")
