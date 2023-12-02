XYZ={"X": 1, "Y": 2, "Z": 3}
winAgainst={"A": "Z", "B": "X", "C": "Y"}
drawAgainst={"A": "X", "B": "Y", "C": "Z"}
loseAgainst={"A": "Y", "B": "Z", "C": "X"}
#A rock X
#B paper Y
#C Scisors Z
with open("2/input.txt", "r") as f:
    points=0
    for row in f:
        row=row.split()

        #X lose
        #Y draw
        #Z win
        if(row[1]=="X"):
            points+=XYZ[winAgainst[row[0]]]
        elif(row[1]=="Y"):
            points+=XYZ[drawAgainst[row[0]]]+3
        elif(row[1]=="Z"):
            points+=XYZ[loseAgainst[row[0]]]+6

        print(points)

print(points)