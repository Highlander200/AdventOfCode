with open("4/input.txt","r") as f:
    cont=0
    for row in f:
        row=row.replace("\n","")
        elves=row.split(",")
        left=elves[0].split("-")
        right=elves[1].split("-")

        if((int(left[0]) in list(range(int(right[0]),int(right[1])+1))) or (int(left[1]) in list(range(int(right[0]),int(right[1])+1)))):
            cont+=1
        elif((int(right[0]) in list(range(int(left[0]),int(left[1])+1))) or (int(right[1]) in list(range(int(left[0]),int(left[1])+1)))):
            cont+=1
        else:
            print(left,right)

print(cont)
