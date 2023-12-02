mat=[]
with open("8/input.txt","r") as f:
    cont=0
    for row in f:
        row=list(row)
        mat.append([])
        for e in row:
            mat[cont].append(e)
        cont+=1

nAlberi=0
for i in range(cont):
    for j in range(99):
        isVisible=True
        y=i-1
        x=j
        while(y>=0): #Verticale in su
            if(mat[y][x]>=mat[i][j]):
                isVisible=False
                break
            y-=1
        if(isVisible):
            print(i,j)
            nAlberi+=1
            continue
        
        isVisible=True
        y=i+1
        x=j
        while(y<cont): #Verticale in giù
            if(mat[y][x]>=mat[i][j]):
                isVisible=False
                break
            y+=1
        if(isVisible):
            print(i,j)
            nAlberi+=1
            continue

        isVisible=True
        y=i
        x=j-1
        while(x>=0): #Orizzontale sinistra
            if(mat[y][x]>=mat[i][j]):
                isVisible=False
                break
            x-=1
        if(isVisible):
            print(i,j)
            nAlberi+=1
            continue

        isVisible=True
        y=i
        x=j+1
        while(x<len(mat[i])): #Orizzontale destra
            if(mat[y][x]>=mat[i][j]):
                isVisible=False
                break
            x+=1
        if(isVisible):
            print(i,j)
            nAlberi+=1
            continue


print(nAlberi)