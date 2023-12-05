map=dict()

{
    ("seed","soil"):[
        ("dest","src","len")
    ]
}

with open("input.txt","r") as f:
    seeds=f.readline().split(":")[1].strip()
    seeds=seeds.split()
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

values=[int(x) for x in seeds]

for transformlist in map.values():
    modified=[False for x in values]
    
    for transform in transformlist:
        dest=transform[0]
        src=transform[1]
        leng=transform[2]
        diff=dest-src
        for i in range(len(values)):
            value=values[i]

            if(modified[i]):
                continue

            if(value>=src and value<src+leng):
                values[i]=value+diff
                modified[i]=True

print(min(values))
