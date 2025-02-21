from randomGraph import randomGraph
from timeit import default_timer as timer
import plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

nMax = 450  #n° massimo di valori che verranno generati in un array da ordinare
tMax = 1800  #tempo massimo consentito di esecuzione (sono 30 minuti) [per evitare di aspettare troppo]

#array che servono per creare i grafici 
timesRandGraphCC = []  #tempi di esecuzione per le componenti connesse di grafi casuali
timesRandGraphK = []  #tempi di esecuzione per MST-Kruskal di grafi casuali
timesWRandGraphCC = []  #tempi di esecuzione per le componenti connesse di grafi casuali pesati
timesWRandGraphK = []  #tempi di esecuzione per le MST-Kruskal di grafi casuali pesati

startTot = timer()  #tempo di esecuzione totale degli algoritmi (NON serve a niente, è per curiosità)

#---GRAFI CASUALI (inizio)---
for i in range(1, nMax):
    min = i  #il n° minimo di archi da generare nel grafo aumenta all'aumentare del n° totale di nodi
    max = i * 2  #il n° massimo di archi da generare nel grafo aumenta all'aumentare del n° totale di nodi
    nArchi = []  #lista del numero di archi effettivamente generati per ogni grafo G

    G = randomGraph(i, min, max, False)  #generazione del grafo casuale (FALSE = NON pesato)

    #crea l'array con tutti i tempi del calcolo delle componenti connesse dei grafi non pesati con numero di nodi da 1 a n=450
    start = timer()
    G.connectedComponents()  #calcolo delle componenti connesse di G
    end = timer()
    timesRandGraphCC.append(end - start)
    if timesRandGraphCC[i - 1] > tMax:
        break

    #crea l'array con tutti i tempi del calcolo di Kruskal dei grafi non pesati con numero di nodi da 1 a n=450
    start = timer()
    G.MSTKruskal()  #generazione di un MST (= minimum spanning tree) per G
    end = timer()
    timesRandGraphK.append(end - start)
    if timesRandGraphK[i - 1] > tMax:
        break

#TABELLA CC + KRUSKAL (grafi non pesati)
#per creare la tabella non si prendono tutti i tempi da 1 a 450, ma si prendono solo i tempi con uno step di 30 in 30 fino a 450
step = 30 #si procede di 30 fino ad arrivare a 450 nodi nel grafo casuale

nNodi = [] #serve alla tabella per indicare il numero di nodi a cui ci riferiamo con un determinato tempo
for j in range(0, nMax, step):
    nNodi.append(j)
nNodi.append(i)

tCC = [] #serve alla tabella per indicare il tempo del calcolo delle componenti connesse (grafi non pesati) a cui ci riferiamo con un determinato tempo
for j in range(0, len(timesRandGraphCC), step):
    tCC.append(round(timesRandGraphCC[j] *1000, 3)) #round serve per approssimare a 3 cifre dopo la virgola
tCC.append(round(timesRandGraphCC[i - 1] *1000, 3)) 

tK = [] #serve alla tabella per indicare il tempo del calcolo di Kruskal (grafi non pesati) a cui ci riferiamo con un determinato tempo
for j in range(0, len(timesRandGraphK), step):
    tK.append(round(timesRandGraphK[j] *1000, 3)) 
tK.append(round(timesRandGraphK[i - 1] *1000, 3))

#generazione tabella .html con libreria plotly
trace = go.Table(header=dict(values=['Nodi', 'Tempo CC (ms)', 'Tempo Kruskal (ms)']),cells=dict(values=[nNodi, tCC, tK,]))  # Nodi, tempi ComponentiConnesse, tempi Kruskal
data = [trace]
py.offline.plot(data, filename='tabella_GrafiNONPesati.html') #metodo plot serve per 'disegnare' la tabella

# GRAFICO CC + KRUSKAL (grafi non pesati)
#genero due grafici uno per componenti connesse e uno per Kruskal nello stesso piano
plt.plot(range(nMax - 1), timesRandGraphCC, 'r') #componenti connesse (grafi non pesati) in rosso
plt.plot(range(nMax - 1), timesRandGraphK, 'g') #kruskal (grafi non pesati) in verde
plt.xlabel("n")
plt.ylabel("tempo (s)")
plt.title("Grafi non pesati, componenti connesse in rosso e Kruskal in verde")
plt.show()
#---GRAFI CASUALI (fine)---

#---GRAFI CASUALI PESATI (inizio)---
for i in range(1, nMax):
    min = i  #il n° minimo di archi da generare nel grafo aumenta all'aumentare del n° totale di nodi
    max = i * 2  #il n° massimo di archi da generare nel grafo aumenta all'aumentare del n° totale di nodi

    G = randomGraph(i, min, max, True)  #generazione del grafo casuale pesato (TRUE = pesato)

    #crea l'array con tutti i tempi del calcolo delle componenti connesse dei grafi pesati con numero di nodi da 1 a n=450
    start = timer()
    G.connectedComponents()  #calcolo delle componenti connesse di G
    end = timer()
    timesWRandGraphCC.append(end - start)
    if timesWRandGraphCC[i - 1] > tMax:
        break

    #crea l'array con tutti i tempi del calcolo di Kruskal dei grafi non pesati con numero di nodi da 1 a n=450
    start = timer()
    G.MSTKruskal()  #generazione di un MST per G
    end = timer()
    timesWRandGraphK.append(end - start)
    
    if timesWRandGraphK[i - 1] > tMax:
        break

#TABELLA CC + KRUSKAL (grafi pesati)
#per creare la tabella non si prendono tutti i tempi da 1 a 450, ma si prendono solo i tempi con uno step di 30 in 30 fino a 450

nNodiW = [] #serve alla tabella per indicare il numero di nodi a cui ci riferiamo con un determinato tempo
for j in range(0, nMax, step):
    nNodiW.append(j)
nNodiW.append(i)

tCCW = [] #serve alla tabella per indicare il tempo del calcolo delle componenti connesse (grafi pesati) a cui ci riferiamo con un determinato tempo
for j in range(0, len(timesWRandGraphCC), step):
    tCCW.append(round(timesWRandGraphCC[j] *1000, 3)) 
tCCW.append(round(timesWRandGraphCC[i - 1] *1000, 3)) 

tKW = [] #serve alla tabella per indicare il tempo del calcolo di Kruskal (grafi pesati) a cui ci riferiamo con un determinato tempo
for j in range(0, len(timesWRandGraphK), step):
    tKW.append(round(timesWRandGraphK[j] *1000, 3)) 
tKW.append(round(timesWRandGraphK[i - 1] *1000, 3)) 

#generazione tabella .html con libreria plotly
trace = go.Table(header=dict(values=['Nodi', 'Tempo CC (ms)', 'Tempo Kruskal (ms)']), cells=dict(values=[nNodiW, tCCW, tKW,]))  #Nodi, t CC (s), t K (s)
data = [trace]
py.offline.plot(data, filename='tabella_GrafiPesati.html')

# GRAFICO CC + KRUSKAL (grafi pesati)
#genero due grafi uno per componenti connesse e uno per Kruskal
plt.plot(range(nMax - 1), timesWRandGraphCC, 'r') #componenti connesse (grafi pesati) in rosso
plt.plot(range(nMax - 1), timesWRandGraphK, 'g') #kruskal (grafi pesati) in verde
plt.xlabel("n")
plt.ylabel("tempo (s)")
plt.title("Grafi pesati, componenti connesse in rosso e Kruskal in verde")
plt.show()
#---GRAFI CASUALI PESATI (fine)---

#conclusione del timer dell'esecuzione totale del programma (NON serve a niente, è per curiosità)
endTot = timer()
totalTime = endTot - startTot
#print(totalTime)
