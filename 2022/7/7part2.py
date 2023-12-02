tree={
    "/": [0]
}
att="/" #Imposta attuale a "/"
with open("7/input.txt","r") as f:
    for row in f:
        row=row.split()
        if(row[0]=="$"): #Se è un comando
            if(row[1]=="cd"): #Se è cd
                if(row[2]=="/"): #Se mi manda in "/"
                    att="/"
                elif(row[2]!=".."): #Se mi da il percorso
                    att+=row[2]+"/"
                else: #Se è ".."
                    att=att[:-1]
                    while(att[-1] != "/"): 
                        att=att[:-1]
            else: #Se è ls
                continue
        else: #Se è risultato di ls
            if(row[0]=="dir"): #Se è una cartella
                path=att+row[1]+"/"
                if(path not in tree): #Se è una nuova cartella
                    tree[path]=[] #Aggiungi all'albero
                    if(att=="/"): #Se siamo nella root
                        tree["/"].append(row[1])
                    else: #Se è una sottocartella
                        tree[att].append(row[1]) #Aggiungi alla cartella superiore
                else: #Se la cartella esiste
                    continue
            else: #Se è un file
                if(att=="/"): #Se siamo nella root
                    tree["/"].append(row[0])
                else:
                    tree[att].append(row[0]) #Aggiungi alla cartella superiore

sizes={}
def som(path):
    somma=0
    for val in tree[path]: #Per ogni valore nella cartella
        if(path+str(val)+"/" in tree): #Se è una cartella
            somma+=som(path+val+"/")
        else: #Se è un file
            somma+=int(val)

    sizes[path]=somma
    return somma

som("/")

minimum=sizes["/"]
spazioNecessario=30000000-(70000000-sizes["/"])
for value in sizes.values():
    if(value>=spazioNecessario and value<=minimum):
        minimum=value

print(minimum)