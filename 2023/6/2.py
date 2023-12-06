with open("input.txt","r") as f:

    time=int(f.readline().split(":")[1].strip().replace(" ",""))
    
    distance=int(f.readline().split(":")[1].strip().replace(" ",""))


som=0
for i in range(time+1):
    myDistance=(time-i)*i
    if(myDistance>distance):
        som+=1


print(som)