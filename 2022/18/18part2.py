import time

input=list()
with open("18/input.txt","r") as f:
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

interns=set()
toRemove=list()

def isIntern(nVisited,cube):
    if(nVisited==10):
        return False
    
    interno=False
    x=cube[0]
    y=cube[1]
    z=cube[2]

    nFaces=0
    for i in range(nCubes):
        x1=input[i][0]
        y1=input[i][1]
        z1=input[i][2]

        diffx=abs(x1-x)
        diffy=abs(y1-y)
        diffz=abs(z1-z)
        if(diffx==0 and diffy==0 and diffz==1):
            nFaces+=1
        elif(diffx==0 and diffy==1 and diffz==0):
            nFaces+=1
        elif(diffx==1 and diffy==0 and diffz==0):
            nFaces+=1

    if(nFaces==6*nVisited-2*nVisited):
        nSides-=6
        interns.add((x,y,z))
        toRemove.append(possible)

    


for possible in possibleIntern:
    x=possible[0]
    y=possible[1]
    z=possible[2]

    if(isIntern(0,possible)):
        nSides-=6



for possible in possibleIntern:
    x=possible[0]
    y=possible[1]
    z=possible[2]
    
    nFaces=0
    for i in range(nCubes):
        x1=input[i][0]
        y1=input[i][1]
        z1=input[i][2]

        diffx=abs(x1-x)
        diffy=abs(y1-y)
        diffz=abs(z1-z)
        if(diffx==0 and diffy==0 and diffz==1):
            nFaces+=1
        elif(diffx==0 and diffy==1 and diffz==0):
            nFaces+=1
        elif(diffx==1 and diffy==0 and diffz==0):
            nFaces+=1

    if(nFaces==6):
        nSides-=6
        interns.add((x,y,z))
        toRemove.append(possible)

for remove in toRemove:
    possibleIntern.remove(remove)

isPossible=True
while(isPossible):
    print("Ciaone")
    isPossible=False
    toRemove=list()

    for intern in interns:
        x1=intern[0]
        y1=intern[1]
        z1=intern[2]

        diffx=abs(x1-x)
        diffy=abs(y1-y)
        diffz=abs(z1-z)
        if(diffx==0 and diffy==0 and diffz==1):
            isPossible=True
            nSides-=6
            interns.add((x,y,z))
            toRemove.append(possible)
        elif(diffx==0 and diffy==1 and diffz==0):
            isPossible=True
            nSides-=6
            interns.add((x,y,z))
            toRemove.append(possible)
        elif(diffx==1 and diffy==0 and diffz==0):
            isPossible=True
            nSides-=6
            interns.add((x,y,z))
            toRemove.append(possible)

    for remove in toRemove:
        possibleIntern.remove(remove)


print(nSides)