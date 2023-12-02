XYZ={"X": 1, "Y": 2, "Z": 3}
winAgainst={"X": "C", "Y": "A", "Z": "B"}
drawAgainst={"X": "A", "Y": "B", "Z": "C"}

with open("2/input.txt", "r") as f:
    points=0
    for row in f:
        row=row.split()
        points+=XYZ[row[1]]
        if(row[0] == winAgainst[row[1]]):
            points+=6
        elif(row[0] == drawAgainst[row[1]]):
            points+=3

print(points)
