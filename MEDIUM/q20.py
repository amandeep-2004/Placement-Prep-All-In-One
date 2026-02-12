s=input("enter the string: ")
d={}
for i in s:
	d[i]=d.get(i,0)+1
if all(v!=1 for v in d.values()):
	print("no non-repeating character found")
	exit()
for v in d:
	if d[v]==1:
		print(f"firdt non repeating charcter in string : {v}")
		break


#second method
f={}
for i in s:
	f[i]=f.get(i,0)+1

for i in s:
	if f[i]==1:
		print(f"first non repeating character : {i}")
		break
else:
	print("no non-repeating character present")