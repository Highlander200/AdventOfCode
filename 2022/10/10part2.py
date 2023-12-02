mat=[
    
]
rowCRT=0
def render(cont,X):
    global rowCRT
    for i in range(6):
        if(cont==40*i):
            rowCRT=i
            mat.append([])
            break
    while(cont>40):
        cont-=40
    if(cont==X-1 or cont==X or cont==X+1):
        mat[rowCRT].append("#")
    else:
        mat[rowCRT].append(".")

with open("10/input.txt","r") as f:
    cont=0
    X=1
    for row in f:
        row=row.replace("\n","").split()
        if(row[0]=="noop"):
            render(cont,X)
            cont+=1
        else:
            render(cont,X)
            cont+=1
            render(cont,X)
            cont+=1
            X+=int(row[1])

for i in range(6):
    print(*mat[i])
