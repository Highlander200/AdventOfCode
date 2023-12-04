numOfCards=dict()

with open("input.txt","r") as f:
    i=0
    for row in f:
        i+=1
        data=row.strip().split(":")[1].split("|")
        data[0]=data[0].replace("  "," ")
        data[1]=data[1].replace("  "," ")
        winners=[x.strip() for x in data[0].split()]
        guesses=[x.strip() for x in data[1].split()]

        if i not in numOfCards:
            numOfCards[i]=0
        numOfCards[i]+=1

        cont=0
        for winner in winners:
            if(winner in guesses):
                cont+=1
        for j in range(i+1,i+cont+1):
            numOfCards[j]=numOfCards.get(j,0)+numOfCards[i]
        

print(sum(numOfCards.values()))
