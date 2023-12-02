rows=[]
visited = set() #set con le coordinate visitate
yh = 0
xh = 0

pos = [(0, 0)] * 10
visited.add(pos[0])

with open("9/input.txt","r") as f:
    for row in f:
        rows.append(row)

for row in rows:
    direction = row.split(" ")[0]
    nMoves = int(row.split(" ")[1])
    for i in range(nMoves):
        copy = [x for x in pos]
        if direction == "U": yh += 1
        if direction == "D": yh -= 1
        if direction == "L": xh -= 1
        if direction == "R": xh += 1
        pos[0] = (yh, xh) #first

        for position in range(1, len(pos)):
            if abs(pos[position][0] - pos[position - 1][0]) > 1 or abs(pos[position][1] - pos[position - 1][1]) > 1:
                pos[position] =(
                    #X
                    pos[position][0] +
                    (1 if pos[position - 1][0] - pos[position][0] > 0
                    else (0 if pos[position - 1][0] - pos[position][0] == 0
                    else -1)),

                    #Y
                    pos[position][1] +
                    (1 if pos[position - 1][1] - pos[position][1] > 0
                    else (0 if pos[position - 1][1] - pos[position][1] == 0
                    else -1))
                )

        visited.add(pos[-1])

print(len(visited))