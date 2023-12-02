points=0
with open("3/input.txt","r") as f:
    for row in f:
        lenght=len(row)
        firstHalf=row[0:int(lenght/2)]
        secondHalf=row[int(lenght/2):lenght]

        alreadyCount=[]
        for char in secondHalf:
            if((char in firstHalf) and (char not in alreadyCount)):
                alreadyCount.append(char)
                punto=ord(char)

                if(punto > 96):
                    punto-=96
                else:
                    punto-=38

                print(punto)
                points+=punto

print(points)