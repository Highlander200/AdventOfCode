som=0

with open("input.txt","r") as f:
    for row in f:
        data=row.strip().split(":")[1].split("|")
        data[0]=data[0].replace("  "," ")
        data[1]=data[1].replace("  "," ")
        winners=[x.strip() for x in data[0].split()]
        guesses=[x.strip() for x in data[1].split()]

        cont=-1
        for winner in winners:
            if(winner in guesses):
                cont+=1
        if(cont!=-1):
            som+=pow(2,cont)

print(som)
