input=list()
nBlueprints=0
with open("19/inputtest.txt","r") as f:
    for row in f:
        nBlueprints+=1
        row=row.split(" ")
        input.append([int(row[6]),int(row[12]),int(row[18]),int(row[21]),int(row[27]),int(row[30])])
#ore cost [ore], clay cost [ore], obsidian cost [ore,clay], geode cost [ore,obsidian]
info=list()

def solve(oreFarm,clayFarm,obsidianFarm,geodeFarm,ore,clay,obsidian,geode,minute):
    if(minute==25):
        return geode

    if((oreFarm,clayFarm,obsidianFarm,geodeFarm,ore,clay,obsidian,geode,minute) in alreadySolved.keys()):
        return alreadySolved[(oreFarm,clayFarm,obsidianFarm,geodeFarm,ore,clay,obsidian,geode,minute)]


    
    maximum=0

    tempOre=ore+oreFarm
    tempClay=clay+clayFarm
    tempObsidian=obsidian+obsidianFarm
    tempGeode=geode+geodeFarm

    if(ore>=info[0]):
        tempOreFarm=oreFarm+1
        maximum=max(maximum,solve(tempOreFarm,clayFarm,obsidianFarm,geodeFarm,tempOre,tempClay,tempObsidian,tempGeode,minute+1))
    if(ore>=info[1]):
        tempClayFarm=clayFarm+1
        maximum=max(maximum,solve(oreFarm,tempClayFarm,obsidianFarm,geodeFarm,tempOre,tempClay,tempObsidian,tempGeode,minute+1))
    if(ore>=info[2] and clay>=info[3]):
        tempObsidianFarm=obsidianFarm+1
        maximum=max(maximum,solve(oreFarm,clayFarm,tempObsidianFarm,geodeFarm,tempOre,tempClay,tempObsidian,tempGeode,minute+1))
    if(ore>=info[4] and obsidian>=info[5]):
        tempGeodeFarm=geodeFarm+1
        maximum=max(maximum,solve(oreFarm,clayFarm,obsidianFarm,tempGeodeFarm,tempOre,tempClay,tempObsidian,tempGeode,minute+1))

    maximum=max(maximum,solve(oreFarm,clayFarm,obsidianFarm,geodeFarm,tempOre,tempClay,tempObsidian,tempGeode,minute+1))

    alreadySolved[(oreFarm,clayFarm,obsidianFarm,geodeFarm,ore,clay,obsidian,geode,minute)]=maximum
    return maximum
solution=0

for i in range(nBlueprints):
    alreadySolved=dict()
    info=input[i]
    solution+=(solve(1,0,0,0,0,0,0,0,0)*(i+1))
print(solution)