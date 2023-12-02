import time

input=list()
with open("18/inputtest.txt","r") as f:
    for row in f:
        row=row.replace("\n","").split(",")
        input.append([int(row[0]),int(row[1]),int(row[2])])
nCubes=len(input)
nSides=nCubes*6
possibleIntern=set()

for i in range(nCubes):
    x=input[i][0]
    y=input[i][1]
    z=input[i][2]

    possibleIntern.add((x+1,y,z))
    possibleIntern.add((x,y+1,z))
    possibleIntern.add((x,y,z+1))
    possibleIntern.add((x-1,y,z))
    possibleIntern.add((x,y-1,z))
    possibleIntern.add((x,y,z-1))

    

    for j in range(nCubes):
        x1=input[j][0]
        y1=input[j][1]
        z1=input[j][2]

        if((x1,y1,z1) in possibleIntern):
            possibleIntern.remove(((x1,y1,z1)))

        diffx=abs(x1-x)
        diffy=abs(y1-y)
        diffz=abs(z1-z)
        if(diffx==0 and diffy==0 and diffz==1):
            nSides-=1
        elif(diffx==0 and diffy==1 and diffz==0):
            nSides-=1
        elif(diffx==1 and diffy==0 and diffz==0):
            nSides-=1

notVisited=possibleIntern
while(len(notVisited)>0):
    totFaces=0
    nVisited=0
    queue=[possibleIntern.pop()]

    while(len(queue)>0 and nVisited<100):
        print(queue)
        nVisited+=1
        att=queue.pop(0)
        x=att[0]
        y=att[1]
        z=att[2]
        nFaces=6
        new=(x+1,y,z)
        if((new not in input) and (new in notVisited)):
            queue.append(new)
            notVisited.remove(new)
            nFaces-=1
            if(new in possibleIntern):
                possibleIntern.remove(new)
        new=(x,y+1,z)
        if((new not in input) and (new in notVisited)):
            queue.append(new)
            notVisited.remove(new)
            nFaces-=1
            if(new in possibleIntern):
                possibleIntern.remove(new)
        new=(x,y,z+1)
        if((new not in input) and (new in notVisited)):
            queue.append(new)
            notVisited.remove(new)
            nFaces-=1
            if(new in possibleIntern):
                possibleIntern.remove(new)
        new=(x-1,y,z)
        if((new not in input) and (new in notVisited)):
            queue.append(new)
            notVisited.remove(new)
            nFaces-=1
            if(new in possibleIntern):
                possibleIntern.remove(new)
        new=(x,y-1,z)
        if((new not in input) and (new in notVisited)):
            queue.append(new)
            notVisited.remove(new)
            nFaces-=1
            if(new in possibleIntern):
                possibleIntern.remove(new)
        new=(x,y,z-1)
        if((new not in input) and (new in notVisited)):
            queue.append(new)
            notVisited.remove(new)
            nFaces-=1
            if(new in possibleIntern):
                possibleIntern.remove(new)
        totFaces+=nFaces
    
    
    if(nVisited<99):
        nSides-=totFaces


print(nSides)