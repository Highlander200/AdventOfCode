mat=[]
visited=[]
distances=[]
xS=-1
yS=0

with open("12/inputTest.txt","r") as f:
    i=0
    for row in f:
        mat.append(list(row))
        visited.append([False for i in range(len(row))])
        distances.append([0 for i in range(len(row))])
        if(xS==-1):
            xS=row.find('S')
            if(xS!=-1):
                yS=i
        i+=1

queue=[[yS,xS]]
distances[yS][xS]=0
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
print(distance)