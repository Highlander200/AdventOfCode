maxx=0
maxy=0
minx=999999999
miny=999999999

input=[]
with open("14/input.txt","r") as f:
    for row in f:
        row=row.replace("\n","").split(" -> ")
        for i in range(len(row)):
            row[i]=row[i].split(",")
            row[i][0]=int(row[i][0])
            row[i][1]=int(row[i][1])

            maxx=max(maxx,row[i][0])
            maxy=max(maxy,row[i][1])
            minx=min(minx,row[i][0])
            miny=min(miny,row[i][1])
        input.append(row)

def printM(matrix):
    for row in matrix:
        print(row)


#COMPILAZIONE MATRICE
startSand=500-minx
mat=[["." for i in range(minx,maxx+1)] for j in range(maxy+1)]

for row in input:
    lastCoord=[row[0][0]-minx,row[0][1]]
    for i in range(1,len(row)):
        coords=[row[i][0]-minx,row[i][1]]
        if(coords[0]!=lastCoord[0]):
            for j in range(min(coords[0],lastCoord[0]),max(coords[0],lastCoord[0])+1):
                mat[coords[1]][j]="#"
            #print(mat[coords[1]][min(coords[0],lastCoord[0]):max(coords[0],lastCoord[0])])
        else:
            for j in range(min(coords[1],lastCoord[1]),max(coords[1],lastCoord[1])+1):
                mat[j][coords[0]]="#"
        lastCoord=coords
#print(minx,maxx,miny,maxy)
#printM(mat)

#SABBIA
def moveSand(y,x):
    if(y>=(len(mat)-1)):
        return False
    if(x<1 or x>=(len(mat[0])-1)):
        return False
    
    if(mat[y+1][x]=="."): #DOWN
        mat[y+1][x]="+"
        mat[y][x]="."
        return moveSand(y+1,x)
    elif(mat[y+1][x-1]=="."): #LEFT-DOWN
        mat[y+1][x-1]="+"
        mat[y][x]="."
        return moveSand(y+1,x-1)
    elif(mat[y+1][x+1]=="."): #RIGHT-DOWN
        mat[y+1][x+1]="+"
        mat[y][x]="."
        return moveSand(y+1,x+1)
    else:
        mat[y][x]="o"
        return True

cont=0
mat[0][startSand]="+"
while(moveSand(0,startSand)):
    cont+=1
printM(mat)
print(cont)