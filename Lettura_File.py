import numpy as np
import pandas as pd
import string 

#Apertura del file contenente le informazioni    
f= open("C:/dev/Mesh1.txt", 'r')
#Lettura di ogni riga del file
file=f.readlines()
#Ordino il file dalla riga 0 all'ultima riga
for i in range(0, len(file)):
    RigaFile=file[i]
    #Alla stringa contenente "NODE COORDINATES" sostituisco il nome stesso
    #come intestazione dei nodi
    if "NODE COORDINATES" in RigaFile:
        print("\n NODE COORDINATES:\n")
    #Ad ogni riga contenente 'Node' viene riportato il testo del file in array
    if "Node " in RigaFile:
        node=RigaFile.split()            #Ogni riga è una lista con elementi 'stringhe'
        n=node[3:6]                  #Estrapolo gli elementi relativi alle coordinate
        n=[(float(i)) for i in n]    #Trasformo le singole stringhe in numeri
        Node=np.array(n)             #Genero vettori per ogni riga
        print(Node)                  #Vettori

    #Stessa cosa per gli elementi   
    if "BEAM ELEMENTS" in RigaFile:
        print("\n BEAM ELEMENTS:\n")
    if "Beam  " in RigaFile:
        beam=RigaFile.split()
        print(beam[1:6])
        
    #Stessa cosa per i vincoli   
    if "NODE RESTRAINTS" in RigaFile:
        print("\n NODE RESTRAINTS:\n")
    if "NdFreedom" in RigaFile:
        restraint=RigaFile.split()
        print(restraint[2])
        
    #Stessa cosa per la pretensione in ogni elemento   
    if "BEAM PRE-LOADS" in RigaFile:
        print("\n BEAM PRE-LOADS:\n")
    if "BmPreLoad" in RigaFile:
        tension=RigaFile.split()
        print(tension[2:4],)

        x=[]                         #Prova costruzione vettore coordinata x                 
        if Node[0]== '1.' in Node:
            X=x.append((Node[0]))
            print(X)
            
a=[]
print("\n Vettore vuoto_prova\n a:\n",a) #Vettore vuoto_prova

x=np.empty((30,1))                   #Vettore vuoto 30x1 per coordinata X 
print("\n COORDINATES\n X:\n",x)
y=np.empty((30,1))                   #Vettore vuoto 30x1 per coordinata Y
print("\n Y:\n",y)
z=np.empty((30,1))                   #Vettore vuoto 30x1 per coordinata Z
print("\n Z:\n",z)

