from unionFind import unionFind
import numpy as np
import random

#Vertice v
#rappresenta il vertice del grafo che creo. Al suo interno contiene semplicemento una chiave per riconoscerlo
class node:
    key = None  #chiave contenuta nel nodo (identificatore)

    def __init__(self, k):
        self.key = k


#Arco (u,v)
#rappresenta l'arco che sta tra due vertici u e v. Inoltre abbiamo il peso che è posto a 0 nel caso di grafi non pesati.
class edge:
    u = None
    v = None
    weight = 0

    def __init__(self, u, v, w):
        self.u = u  # u
        self.v = v  # v
        self.weight = w  #peso dell'arco


#Generatore di grafi casuali
#con componenti connesse
#e MST-Kruskal
class randomGraph:
    nodes = []  #lista dei vertici
    edges = []  #lista degli archi
    n: int  #n° vertici del grafo
    adjMatrix: np.zeros  #matrice di adiacenza (per rappresentare i grafi)
    unionFind = unionFind() #struttura dati UnionFind 

    def __init__(self, n, min, max, w): #w serve per indicare se il grafo è pesato o no
        self.n = n #n° vertici del grafo
        self.adjMatrix = np.zeros((n, n))  #inizialmente la matrice di adiacenza è fatta solo di zeri
        self.unionFind = unionFind() #struttura dati UnionFind (inizialmente vuota)

        #Controlli sull'input
        #min è il minimo di archi da generare nel grafo
        #max è il n° massimo di archi da generare nel grafo
        if max > n:  #controllo su max
            max = n
        if min < 0:  #controllo su min
            min = 0
        if min > max:  #altro controllo su min
            min = n * n

        #Matrice di adiacenza
        k = random.randint(min, n * max)  #sceglie casualmente il n° di archi da creare, tra min e max*n (minimo 0, massimo n*n)
        i = 0  #contatore degli archi creati
        while (i < k):
            x = random.randint(0, n - 1)  #scelta casuale della riga (della matrice di adiacenza) a cui assegnare l'arco
            y = random.randint(0, n - 1)  #scelta casuale della colonna (della matrice di adiacenza) a cui assegnare l'arco
            if self.adjMatrix[x][y] == 0:  #se l'arco non è ancora stato creato
                if w == True:  #se il grafo è pesato
                    self.adjMatrix[x][y] = random.randint(1, 16)  #peso casuale tra 1 e 15 (inclusi) se il grafo è pesato (w = True) - NB: 1 e 16 sono scelti arbitrariamente
                else:
                    self.adjMatrix[x][y] = 1  #arco semplice (peso = 1) altrimenti (w = False)
                i = i + 1

        #Nodi
        self.nodes = []  #lista dei nodi
        for i in range(self.n):
            self.nodes.append(node(i))  #crea la lista dei nodi

        #Archi
        self.edges = []  #lista degli archi
        for i in range(self.n):  #doppio ciclo sulla matrice di adiacenza: esplora ogni singolo valore (= arco)
            for j in range(self.n):
                if self.adjMatrix[i, j] != 0:  #aggiunge l'arco se il valore nella matrice di adiacenza è diverso da zero (ovvero se l'arco esiste)
                    self.edges.append(edge(self.nodes[j], self.nodes[i], self.adjMatrix[i, j]))

    #Algoritmo di Kruskal
    #per ottenere mst (=albero di connessione minimo), questo algoritmo trova un arco sicuro da aggiungere alla foresta in costruzione scegliendo, fra tutti gli archi che collegano due alberi quelsiasi, un arco con peso minimo. A tal fine sfrutta unionFind per mantenere vari insiemi disgiunti di elementi. Alla fine restituisce mst. E' GOLOSO
    def MSTKruskal(self):
        self.unionFind = unionFind() #struttura dati UnionFind
        A = []  #albero delle componenti connesse, inizialmente vuoto
        for node in self.nodes:  #per ogni vertice del grafo
            self.unionFind.makeSet(node)  #crea un insieme (che inizialmente contiene solo quel nodo) utilizzando makeSet
        sortedEdges = sorted(self.edges, key=lambda x: x.weight)  #ordina gli archi in senso non decrescente rispetto al peso (weight)
        for edge in sortedEdges:  #per ogni arco preso in ordine non decrescente
            if self.unionFind.findSet(edge.u) != self.unionFind.findSet(edge.v):  #se u appartiene ad un insieme diverso da quello di v
                A.append((edge.u.key, edge.v.key))  #aggiunge l'arco all'albero A
                self.unionFind.union(edge.u, edge.v)  #ed esegue l'unione tra u e v
        return A  #ritorna l'albero A, che alla fine è diventato un MST del grafo iniziale

    #Componenti connesse
    #calcola le componenti connesse sfruttando le operazioni di UnionFind (non sfrutta il peso del grafo)
    def connectedComponents(self):
        self.unionFind = unionFind() #struttura dati UnionFind
        for node in self.nodes:  #per ogni vertice del grafo
            self.unionFind.makeSet(node)  #crea un insieme (che inizialmente contiene solo quel nodo) utilizzando makeSet
        for edge in self.edges:  #per ogni arco (u,v)
            if self.unionFind.findSet(edge.u) != self.unionFind.findSet(edge.v):  #se u appartiene ad un insieme diverso da quello di v
                self.unionFind.union(edge.u, edge.v)  #esegue l'unione tra u e v (dato che sono collegati dall'arco (u,v))
