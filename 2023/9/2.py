som=0
with open("input.txt","r") as f:
    for row in f:
        data=list()
        data.append([int(x) for x in row.strip().split(" ")])
        
        while(not all(x==0 for x in data[-1])):
            data.append([data[-1][i+1]-data[-1][i] for i in range(len(data[-1])-1)])

        data[-1].insert(0,0)
        for i in range(len(data)-2,-1,-1):
            data[i].insert(0,data[i][0]-data[i+1][0])
        som+=data[0][0]

print(som)

