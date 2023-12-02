input=[]
minx=99999999999
maxx=0
miny=99999999999
maxy=0

with open("15/inputprof.txt","r") as f:
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

indexRow=2000000
#indexRow=10
importantRow=["." for x in range(minx-1000000,maxx+1000000)]

for row in input:
    xS=row[0]
    yS=row[1]
    xB=row[2]
    yB=row[3]
    if(yS==indexRow):
        importantRow[xS-minx]="S"
    if(yB==indexRow):
        importantRow[xB-minx]="B"

    distFromB=abs(xS-xB)+abs(yS-yB)
    distFromRow=abs(indexRow-yS)
    widthRange=distFromB-distFromRow
    if widthRange<0:
        continue
    for i in range(widthRange+1):
        if(importantRow[xS-minx+i]!="S" and importantRow[xS-minx+i]!="B"):
            importantRow[xS-minx+i]="#"
        if(importantRow[xS-minx-i]!="S" and importantRow[xS-minx-i]!="B"):
            importantRow[xS-minx-i]="#"

print(importantRow.count("#"))