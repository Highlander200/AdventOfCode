stacks=[
    ["F","C","P","G","Q","R"],
    ["W","T","C","P"],
    ["B","H","P","M","C"],
    ["L","T","Q","S","M","P","R"],
    ["P","H","J","Z","V","G","N"],
    ["D","P","J"],
    ["L","G","P","Z","F","J","T","R"],
    ["N","L","H","C","F","P","T","J"],
    ["G","V","Z","Q","H","T","C","W"]
]

with open("5/input.txt","r") as f:
    for row in f:
        row=row.split()
        query=[int(row[1]),int(row[3])-1,int(row[5])-1]
        temp=[]
        for i in range(query[0]):
            temp.append(stacks[query[1]].pop())
        for i in range(query[0]):
            stacks[query[2]].append(temp.pop())
ris=""
for stack in stacks:
    ris+=stack[-1]
print(ris)
