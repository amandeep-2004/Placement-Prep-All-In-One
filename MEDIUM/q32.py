#Activity selection: given start[] and end[] of meetings, find max number of non-overlapping meetings.

start = [1, 3, 5]
end   = [3, 5, 7]





pair=[]
for i in range(len(start)):
    t=tuple((start[i],end[i]))
    pair.append(t)
#print(pair)
pair.sort(key=lambda x:x[1])

#print(pair)
key=pair[0][1]
res=[]
res.append(pair[0])
for i in range(1,len(pair)):
    #print(i)
    if pair[i][0]>=key:
        res.append(pair[i])
        key=pair[i][1]
    
    else:
        continue
  
print(res)
print(len(res))
