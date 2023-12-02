mat=[]
visited=[]
distances=[]

with open("12/inputTest.txt","r") as f:
    for row in f:
        mat.append(list(row))
        visited.append([False for i in range(len(row))])
        distances.append([0 for i in range(len(row))])
minDistances=[]
minDis=10000
for i in range(len(mat)):
    yS=i
    xS=0
    queue=[[yS,xS]]
    distances=[[0 for k in range(len(mat[0]))] for j in range(len(mat))]
    visited=[[False for k in range(len(mat[0]))] for j in range(len(mat))]
    visited[yS][xS]=True
    distance=0
    mat[yS][xS]='a'
    while(len(queue)>0):
        v=queue.pop(0) #v=[y,x]
        y=v[0]
        x=v[1]
        #UP
        if (y-1>=0):
            if(mat[y-1][x]=="E"):
                distance=distances[y][x]+1
                break
            elif(ord(mat[y-1][x])<=ord(mat[y][x])+1 and visited[y-1][x]==False):
                visited[y-1][x]=True
                distances[y-1][x]=distances[y][x]+1
                queue.append([y-1,x])
        #DOWN
        if (y+1<len(mat)):
            if(mat[y+1][x]=="E"):
                distance=distances[y][x]+1
                break
            elif(ord(mat[y+1][x])<=ord(mat[y][x])+1 and visited[y+1][x]==False):
                visited[y+1][x]=True
                distances[y+1][x]=distances[y][x]+1
                queue.append([y+1,x])
        #LEFT
        if (x-1>=0):
            if(mat[y][x-1]=="E"):
                distance=distances[y][x]+1
                break
            elif(ord(mat[y][x-1])<=ord(mat[y][x])+1 and visited[y][x-1]==False):
                visited[y][x-1]=True
                distances[y][x-1]=distances[y][x]+1
                queue.append([y,x-1])
        #RIGHT
        
        if (x+1<len(mat[0])):
            if(mat[y][x+1]=="E"):
                distance=distances[y][x]+1
                break
            elif(ord(mat[y][x+1])<=ord(mat[y][x])+1 and visited[y][x+1]==False):
                visited[y][x+1]=True
                distances[y][x+1]=distances[y][x]+1
                queue.append([y,x+1])
    if(distance!=0):
        if(distance<minDis):
            minDistances=distances
            startx=xS
            starty=yS
        minDis=min(minDis,distance)

print(yS,xS)
print(minDistances,minDis)