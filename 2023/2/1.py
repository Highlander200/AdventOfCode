maxim={
    "red":12,
    "green":13,
    "blue":14,
}

som=0
with open("input.txt","r") as f:
    
    for row in f:
        error=False
        i=int(row.split(":")[0].split(" ")[1])
        row=row.split(":")[1].strip()
        records=row.split(";")
        for e in records:
            e=e.strip().split(",")
            for color in e:
                color=color.strip().split(" ")
                n=int(color[0])
                colour=color[1]

                if(n>maxim[colour]):
                    error=True

        if(not error):
            som+=i
    
print(som)