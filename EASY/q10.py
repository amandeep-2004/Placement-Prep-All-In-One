#Check anagram of two strings (without sorting if possible, use freq counting).

s1="silent"
s2="listen"

if len(s1)!=len(s2):
    print("not anagram")
    exit(1)
freq={}
for i in s1:
    freq[i]=freq.get(i,0)+1

for i in s2:
    if i not in freq:
        print("not anagram")
        exit()
    freq[i]-=1

if all(v==0 for v in freq.values()):
    print("anagram")
else:
    print("not anagram")
