paths=dict()
with open("input.txt","r") as f:
    commands=f.readline().strip()
    f.readline()
    
    data=f.readline().strip()
    while(data!=""):
        data=data.split("=")
        data[1]=data[1].strip().replace("(","").replace(")","").split(", ")
        paths[data[0].strip()]=(data[1][0],data[1][1])

        data=f.readline().strip()

atts="AAA"
i=0

while(att!="ZZZ"):
    if(commands[i%len(commands)]=="L"):
        att=paths[att][0]
    else:
        att=paths[att][1]
    i+=1

print(i)
