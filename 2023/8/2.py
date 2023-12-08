import math
import itertools


paths=dict()
with open("input.txt","r") as f:
    commands=f.readline().strip()
    f.readline()
    
    data=f.readline().strip()
    while(data!=""):
        data=data.split("=")
        data[1]=data[1].strip().replace("(","").replace(")","").split(", ")
        paths[data[0].strip()]=(data[1][0],data[1][1])

        data=f.readline().strip()

atts=list()
for e in paths.keys():
    if(e[-1]=="A"):
        atts.append(e)

done=[False for x in atts]
values=[list() for x in atts]
i=0
last=0
while(not all(done)):
    command=commands[i%len(commands)]
    for j in range(len(atts)):
        att=atts[j]

        if(done[j]==True):
           continue

        if(command=="L"):
            atts[j]=paths[att][0]
        else:
            atts[j]=paths[att][1]
        
        if(atts[j][-1]=="Z"):
        
            
            if(any((i%value)==1 for value in values[j])):
                done[j]=True
                #values[j].append(i)
                pass
            else:
                values[j].append(i)
                
            #print(values[j][-1]%values[j][0])
            #print(values)
    i+=1

print(values)
lcms=dict()

lcm=1
for x in values:
    lcm=math.lcm(lcm,x[0]+1)
for i in range(len(values)):
    for j in range(len(values[i])):
        lcms[(i,j)]=math.lcm(lcms.get((i,j),1),values[i][j])
print(lcm)
