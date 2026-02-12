#Reverse words in a sentence: "i love coding" → "coding love i" (trim extra spaces).

s="i love coding"
a=s.split()
l=len(a)
st=" "
for i in range(l-1,-1,-1):
    st+=a[i]+" "
print(st.strip())