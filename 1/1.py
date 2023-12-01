with open("input.txt","r") as f:
    som=0
    for row in f:
        for char in row:
            if(char.isdigit()):
                n1=char
                break
        for char in reversed(row):
            if(char.isdigit()):
                n2=char
                break
        som+=int(n1+n2)

print(som)