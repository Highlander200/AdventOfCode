from multipledispatch import dispatch

map=dict()

{
    ("seed","soil"):[
        ("dest","src","len")
    ]
}

@dispatch(int,int,int)
def inRange(n,startR,endR):
    return n>=startR and n<endR

@dispatch(int,int,int,int)
def inRange(start,end,startR,endR):
    return start>=startR and end<=endR


values=list()

with open("input.txt","r") as f:
    seeds=f.readline().split(":")[1].strip()
    seeds=seeds.split()
    for i in range(len(seeds)//2):
        values.append((seeds[i],seeds[i+1]))
    f.readline()

    for i in range(7):
        row=f.readline()
        actmap=row.split()[0]
        key=(actmap[0],actmap[2])
        map[key]=list()
        data=f.readline().strip()
        while data!="":
            values=data.split()
            map[key].append((int(values[0]),int(values[1]),int(values[2])))
            data=f.readline().strip()

for transformlist in map.values():
    print(transformlist)
    newValues=list()
    
    for transform in transformlist:
        dest=transform[0]
        src=transform[1]
        lenTransf=transform[2]
        endSrc=src+lenTransf
        diff=dest-src
        for i in range(len(values)):
            value=values[i]

            start=value[0]
            lenVal=value[1]
            endVal=start+lenVal

            if(inRange(start,endVal,src,endSrc)):
                newValues.append=(start+diff,lenVal)
            elif(inRange(start,src,endSrc) and (not inRange(endVal,src,endSrc))):
                newValues.append=(start+diff,endSrc+diff)
                newValues.append=(endSrc,endVal)
            elif(start<src and endVal<endSrc)
    values=newValues.copy()
print(min(values))
