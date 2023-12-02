with open("4/input.txt","r") as f:
    cont=0
    for row in f:
        row=row.replace("\n","")
        elves=row.split(",")
        left=elves[0].split("-")
        right=elves[1].split("-")

        if((int(left[0])>=int(right[0]) and int(left[1])<=int(right[1])) or (int(left[0])<=int(right[0]) and int(left[1])>=int(right[1]))):
            print(left,right)
            cont+=1

print(cont)
