som=0
def check(cont,X):
    for i in range(6):
        if(cont==20+40*i):
            global som
            som+=cont*X
            break

with open("10/input.txt","r") as f:
    cont=0
    X=1
    for row in f:
        row=row.replace("\n","").split()
        if(row[0]=="noop"):
            cont+=1
            check(cont,X)
        else:
            cont+=1
            check(cont,X)
            cont+=1
            check(cont,X)
            X+=int(row[1])
print(som)