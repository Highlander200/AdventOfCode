mat=[]
with open("8/input.txt","r") as f:
    cont=0
    for row in f:
        row=row.replace("\n","")
        row=list(row)
        mat.append([])
        for e in row:
            mat[cont].append(e)
        cont+=1

maxPoint=0
for i in range(cont):
    for j in range(99):
        contUp=0
        y=i-1
        x=j
        while(y>=0): #Verticale in su
            contUp+=1
            if(mat[y][x]>=mat[i][j]):
                break
            y-=1
        
        contDown=0
        y=i+1
        x=j
        while(y<cont): #Verticale in giù
            contDown+=1
            if(mat[y][x]>=mat[i][j]):
                break
            y+=1

        contLeft=0
        y=i
        x=j-1
        while(x>=0): #Orizzontale sinistra
            contLeft+=1
            if(mat[y][x]>=mat[i][j]):
                break
            x-=1

        contRight=0
        y=i
        x=j+1
        while(x<len(mat[i])): #Orizzontale destra
            contRight+=1
            if(mat[y][x]>=mat[i][j]):
                break
            x+=1

        point=contRight*contDown*contLeft*contUp
        maxPoint=max(maxPoint,point)

print(maxPoint)