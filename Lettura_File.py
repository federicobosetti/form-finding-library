import numpy as np
import pandas as pd
import string 

#definizione matrici vuote e contatori nodi / aste / vincoli eccetera
numNodes = 0
numBeams = 0
numRestraints = 0
numPreloads = 0
forceDensityLoadCaseID = 0

nodesT=[]
beamsT=[]
restraintsT=[]
beamPreloadsT=[]

#Apertura del file contenente le informazioni    
f= open("Mesh1.txt", 'r')
#Lettura di ogni riga del file
file=f.readlines()
#LEGGO il file dalla riga 0 all'ultima riga



for i in range(0, len(file)):
    rigaFile=file[i]
    rigaSplitted = rigaFile.split()

    if len(rigaSplitted)==0:
            continue


    #Ad ogni riga contenente 'Node' viene riportato il testo del file in array
    if rigaSplitted[0] == "Node":
        numNodes= numNodes + 1
        idNodo = int(rigaSplitted[1])
        # Estrapolo gli elementi relativi alle coordinate
        coordXYZ=list(np.float_(rigaSplitted[3:6]))       #float(rigaSplitted[3:6])
        # aggiungo righe a matrice nodi
        nodesT.append([idNodo] + coordXYZ)
        print(nodesT[-1])

    if rigaSplitted[0] == "Beam":
        numBeams= numBeams + 1
        # Estrapolo la connettività asta
        idBeam = int(rigaSplitted[1])
        node1= int(rigaSplitted[5])
        node2= int(rigaSplitted[6])
        # aggiungo righe a matrice aste
        beamsT.append([idBeam, node1, node2])
        print(beamsT[-1])

    if rigaSplitted[0] == "LoadCase":
        loadCaseName = rigaSplitted[3]
        if loadCaseName=="\"force_densities\"":
            forceDensityLoadCaseID=int(rigaSplitted[1])
            print(["forceDensityLoadCaseID = ", forceDensityLoadCaseID])


    if rigaSplitted[0] == "BmPreLoad":
        loadCaseID = rigaSplitted[1]

        if loadCaseID==forceDensityLoadCaseID:

            numPreloads= numPreloads + 1
            # Estrapolo i pre force
            idBeamPreload = int(rigaSplitted[1])
            idBeam= int(rigaSplitted[2])
            forceDensityValue= float(rigaSplitted[4])
            # aggiungo righe a matrice precarichi
            beamPreloadsT.append([idBeam, forceDensityValue])
            print(beamPreloadsT[-1])

    """
   
    #Stessa cosa per gli elementi   
    if "BEAM ELEMENTS" in rigaFile:
        print("\n BEAM ELEMENTS:\n")
    if "Beam  " in rigaFile:
        beam=rigaFile.split()
        print(beam[1:6])
        
    #Stessa cosa per i vincoli   
    if "NODE RESTRAINTS" in rigaFile:
        print("\n NODE RESTRAINTS:\n")
    if "NdFreedom" in rigaFile:
        restraint=rigaFile.split()
        print(restraint[2])
        
    #Stessa cosa per la pretensione in ogni elemento   
    if "BEAM PRE-LOADS" in rigaFile:
        print("\n BEAM PRE-LOADS:\n")
    if "BmPreLoad" in rigaFile:
        tension=rigaFile.split()
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

"""


