input=list()
with open("18/input.txt","r") as f:
    for row in f:
        row=row.replace("\n","").split(",")
        input.append([int(row[0]),int(row[1]),int(row[2])])
nCubes=len(input)
nSides=nCubes*6

for i in range(nCubes):
    x=input[i][0]
    y=input[i][1]
    z=input[i][2]
    for j in range(nCubes):
        x1=input[j][0]
        y1=input[j][1]
        z1=input[j][2]

        diffx=abs(x1-x)
        diffy=abs(y1-y)
        diffz=abs(z1-z)
        if(diffx==0 and diffy==0 and diffz==1):
            nSides-=1
        elif(diffx==0 and diffy==1 and diffz==0):
            nSides-=1
        elif(diffx==1 and diffy==0 and diffz==0):
            nSides-=1
print(nSides)