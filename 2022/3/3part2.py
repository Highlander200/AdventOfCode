points=0
with open("3/input.txt","r") as f:
    i=0
    elves=[]
    for row in f:
        i+=1
        elves.append(row)

        if(i==3):
            for e in elves[0]:
                if ((e in elves[1]) and (e in elves[2])):
                    punto=ord(e)
                    if(punto > 96):
                        punto-=96
                    else:
                        punto-=38
                    points+=punto
                    break
            i=0
            elves=[]          

print(points)