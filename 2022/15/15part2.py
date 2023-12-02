input=[]
minx=99999999999
maxx=0
miny=99999999999
maxy=0
distances=[]

with open("15/input.txt","r") as f:
    for row in f:
        row=row.replace("\n","").split(":")
        row[0]=row[0].split("=")
        row[1]=row[1].split("=")
        row[1][1]=row[1][1].split(",")
        row[0][1]=row[0][1].split(",")

        input.append([int(row[0][1][0]),int(row[0][2]), int(row[1][1][0]),int(row[1][2])])
        minx=min(minx,min(input[-1][0],input[-1][2]))
        maxx=max(maxx,max(input[-1][0],input[-1][2]))
        miny=min(miny,min(input[-1][1],input[-1][3]))
        maxy=max(maxy,max(input[-1][1],input[-1][3]))
        distances.append(abs(input[-1][0]-input[-1][2])+abs(input[-1][1]-input[-1][3]))


area=4000000
#area=20


def isBeacon(y,x):
    isAllFar=True
    for i in range(len(input)):
        xS=input[i][0]
        yS=input[i][1]
        distFromPoint=abs(yS-y)+abs(xS-x)
        if(distFromPoint<=distances[i]):
            isAllFar=False
    return isAllFar

def solve():
    for i in range(0,area):
        print(i)
        for j in range(0,area):
            if(isBeacon(i,j)):
                print(j*4000000+i)
                exit()

solve()