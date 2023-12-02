listAdj=dict()
flowRates=dict()
openedValves=dict()
visited=dict()
with open("16/input.txt","r") as f:
    for row in f:
        row=row.replace("\n","").split(";")
        flowRate=row[0].split("=")[1]
        valve=row[0].split()[1]
        destinations=row[1].replace("valve ","valves ").split("valves ")[1].split(", ")
        listAdj[valve]=[]
        flowRates[valve]=int(flowRate)
        openedValves[valve]=False
        visited[valve]=0
        for destination in destinations:
            listAdj[valve].append(destination)
#print(listAdj,flowRates)
alreadySolved=dict()
start="AA"


def solve(valve1,valve2,flow,minute):
    if(minute==27):
        return flow

    if((valve1,valve2,flow,minute) in alreadySolved.keys()):
        return alreadySolved[(valve1,valve2,flow,minute)]

    for openValve in openedValves.keys():
        if(openedValves[openValve]):
            flow+=flowRates[openValve]

    flowRate1=flowRates[valve1]
    flowRate2=flowRates[valve2]
    maximum=0

    if(flowRate1!=0 and not openedValves[valve1]):
        openedValves[valve1]=True
        maximum=max(maximum,solve(valve1,valve2,flow,minute+1))
        openedValves[valve1]=False

    for dest in listAdj[valve]:
        if(visited[dest]==2):
            continue
        visited[dest]+=1
        maximum=max(maximum,solve(dest,flow,minute+1))
        visited[dest]-=1
    alreadySolved[(valve,flow,minute)]=maximum

    return maximum

print(solve(start,0,1))