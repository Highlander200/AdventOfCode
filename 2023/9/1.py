som=0
with open("input.txt","r") as f:
    for row in f:
        data=list()
        data.append([int(x) for x in row.strip().split(" ")])
        
        while(not all(x==0 for x in data[-1])):
            data.append([data[-1][i+1]-data[-1][i] for i in range(len(data[-1])-1)])

        data[-1].append(0)
        for i in range(len(data)-2,-1,-1):
            data[i].append(data[i+1][-1]+data[i][-1])
        som+=data[0][-1]
        
print(som)

