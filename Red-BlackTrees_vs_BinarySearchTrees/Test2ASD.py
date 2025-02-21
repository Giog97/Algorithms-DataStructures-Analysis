import ABR
import ARN
from timeit import default_timer as timer
import time
import random
import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go

#----Generatore di array random (INIZIO)----
def randomArray(n):
    #Permutazione casuale dei primi n interi
    A = list(range(n))
    random.shuffle(A)
    return A

#----Grafici con i vari casi----
def graficiTuttiICasi():
    nMax = 1000  # n° massimo dei nodi per albero
    timeMax = time.time() + 30*60 #30 minuti è il tempo max
    nMedia = 10 #è il numero di volte che calcoliamo il tempo di esecuzione per un certo numero di valori, per poter poi fare la media
    
    tempiPerGraficoPeggioreInserimento_ABR = [] # tempi di esecuzione per l'inserimento nel caso peggiore ABR per grafico
    tempiPerGraficoPeggioreRicerca_ABR = [] # tempi di esecuzione per la ricerca nel caso peggiore ABR per grafico
    
    tempiPerGraficoInserimentoCasuale_ABR = [] # tempi di esecuzione per l'inserimento nel caso medio ABR per grafico
    tempiPerGraficoRicercaCasuale_ABR = [] # tempi di esecuzione per la ricerca nel caso medio ABR per grafico
    tempiPerGraficoAttraversamentoCasuale_ABR = [] # tempi di esecuzione per l'attraversamento inorder nel caso medio ABR
    
    tempiPerGraficoPeggioreInserimento_ARN = [] # tempi di esecuzione per l'inserimento nel caso peggiore ARN per grafico
    tempiPerGraficoPeggioreRicerca_ARN = [] # tempi di esecuzione per la ricerca nel caso peggiore ARN per grafico
    
    tempiPerGraficoInserimentoCasuale_ARN = [] # tempi di esecuzione per l'inserimento nel caso medio ARN per grafico
    tempiPerGraficoRicercaCasuale_ARN = [] # tempi di esecuzione per la ricerca nel caso medio ARN per grafico
    tempiPerGraficoAttraversamentoCasuale_ARN = [] # tempi di esecuzione per l'attraversamento inorder nel caso medio ARN
    
    mediaAltezzaAlberoPeggiore_ABR = [] # media altezze degli alberi usati ABR caso peggiore
    mediaAltezzaAlberoCasuale_ABR = [] # media altezze degli alberi usati ABR caso medio
        
    mediaAltezzaAlberoPeggiore_ARN = [] # media altezze degli alberi usati ARN caso peggiore
    mediaAltezzaAlberoCasuale_ARN = [] # media altezze degli alberi usati ARN caso medio
    
    for i in range(1, nMax):
        tSommaPerMediaPeggioreInserimento_ABR = 0
        tSommaPerMediaPeggioreRicerca_ABR = 0
        
        tSommaPerMediaInserimentoCasuale_ABR = 0
        tSommaPerMediaRicercaCasuale_ABR = 0
        tSommaPerMediaAttraversamentoCasuale_ABR = 0
        
        tSommaPerMediaPeggioreInserimento_ARN = 0
        tSommaPerMediaPeggioreRicerca_ARN = 0
        
        tSommaPerMediaInserimentoCasuale_ARN = 0
        tSommaPerMediaRicercaCasuale_ARN = 0
        tSommaPerMediaAttraversamentoCasuale_ARN = 0
        
        sommaPerMediaAltezzaAlberoPeggiore_ABR = 0
        sommaPerMediaAltezzaAlberoCasuale_ABR = 0
        
        sommaPerMediaAltezzaAlberoPeggiore_ARN = 0
        sommaPerMediaAltezzaAlberoCasuale_ARN = 0
        
        for k in range(1, nMedia):

            #-----ALBERI BINARI DI RICERCA-----
            #CASO PEGGIORE ABR (array di nodi con chiavi in ordine crescente)
            nodiPeggiori = [] 
            ABRtree = ABR.ABR()
            for j in range(0, i):
                x = ABR.NodoABR(j)
                nodiPeggiori.append(x)

            #CASO PEGGIORE ABR INSERT
            start = timer()
            for j in range(0, len(nodiPeggiori) - 1):
                ABRtree.insert(nodiPeggiori[j])
            end = timer()
            tSommaPerMediaPeggioreInserimento_ABR = tSommaPerMediaPeggioreInserimento_ABR + (end - start)

            #CASO PEGGIORE ABR SEARCH
            start = timer() 
            ABRtree.search(i) # ricerca l'ultimo elemento (in fondo all'albero)
            end = timer()
            tSommaPerMediaPeggioreRicerca_ABR = tSommaPerMediaPeggioreRicerca_ABR + (end - start)
            
            #CASO PEGGIORE ABR HEIGHT
            sommaPerMediaAltezzaAlberoPeggiore_ABR = sommaPerMediaAltezzaAlberoPeggiore_ABR + ABRtree.height()

            #CASO MEDIO ABR (array di nodi con chiavi random)
            nodiCasuali = []  
            ABRtree2 = ABR.ABR()
            A = randomArray(i)
            for j in range(0, len(A)-1):
                x = ABR.NodoABR(A[j])
                nodiCasuali.append(x)

            #CASO MEDIO ABR INSERT
            start = timer() 
            for j in range(0, len(nodiCasuali) - 1):
                ABRtree2.insert(nodiCasuali[j])
            end = timer()
            tSommaPerMediaInserimentoCasuale_ABR = tSommaPerMediaInserimentoCasuale_ABR + (end - start)

            #CASO MEDIO ABR SEARCH
            start = timer() 
            ABRtree2.search(i) # ricerca l'ultimo elemento (in fondo all'albero)
            end = timer()
            tSommaPerMediaRicercaCasuale_ABR = tSommaPerMediaRicercaCasuale_ABR + (end - start)

            #ABR WALK
            start = timer() 
            ABRtree2.inorder()
            end = timer()
            tSommaPerMediaAttraversamentoCasuale_ABR = tSommaPerMediaAttraversamentoCasuale_ABR + (end - start)
            
            #CASO MEDIO ABR HEIGHT
            sommaPerMediaAltezzaAlberoCasuale_ABR = sommaPerMediaAltezzaAlberoCasuale_ABR + ABRtree2.height()


            #-----ALBERI ROSSO NERI-----
            ARNtree = ARN.ARN()

            #CASO "PEGGIORE" ARN INSERT (array di nodi con chiavi in ordine crescente)
            start = timer() 
            for j in range(0, len(nodiPeggiori) - 1):
                ARNtree.insert(nodiPeggiori[j])
            end = timer()
            tSommaPerMediaPeggioreInserimento_ARN = tSommaPerMediaPeggioreInserimento_ARN + (end - start)

            #CASO "PEGGIORE" ARN SEARCH
            start = timer() 
            ARNtree.search(i) # ricerca l'ultimo elemento (in fondo all'albero)
            end = timer()
            tSommaPerMediaPeggioreRicerca_ARN = tSommaPerMediaPeggioreRicerca_ARN + (end - start)
            
            #CASO PEGGIORE ARN HEIGHT
            sommaPerMediaAltezzaAlberoPeggiore_ARN = sommaPerMediaAltezzaAlberoPeggiore_ARN + ARNtree.height()

            ARNtree2 = ARN.ARN()

            #CASO MEDIO ARN INSERT (array di nodi con chiavi random)
            start = timer() 
            for j in range(0, len(nodiCasuali) - 1):
                ARNtree2.insert(nodiCasuali[j])
            end = timer()
            tSommaPerMediaInserimentoCasuale_ARN = tSommaPerMediaInserimentoCasuale_ARN + (end - start)

             #CASO MEDIO ARN SEARCH
            start = timer()
            ARNtree2.search(i) # ricerca l'ultimo elemento (in fondo all'albero)
            end = timer()
            tSommaPerMediaRicercaCasuale_ARN = tSommaPerMediaRicercaCasuale_ARN + (end - start)

            #ARN WALK
            start = timer() 
            ARNtree2.inorder()
            end = timer()
            tSommaPerMediaAttraversamentoCasuale_ARN = tSommaPerMediaAttraversamentoCasuale_ARN + (end - start)
            
            #CASO MEDIO ABR HEIGHT
            sommaPerMediaAltezzaAlberoCasuale_ARN = sommaPerMediaAltezzaAlberoCasuale_ARN + ARNtree2.height()
            
        
        tempiPerGraficoPeggioreInserimento_ABR.append(tSommaPerMediaPeggioreInserimento_ABR/nMedia)
        tempiPerGraficoPeggioreRicerca_ABR.append(tSommaPerMediaPeggioreRicerca_ABR/nMedia)
        
        tempiPerGraficoInserimentoCasuale_ABR.append(tSommaPerMediaInserimentoCasuale_ABR/nMedia)
        tempiPerGraficoRicercaCasuale_ABR.append(tSommaPerMediaRicercaCasuale_ABR/nMedia)
        tempiPerGraficoAttraversamentoCasuale_ABR.append(tSommaPerMediaAttraversamentoCasuale_ABR/nMedia)
        
        tempiPerGraficoPeggioreInserimento_ARN.append(tSommaPerMediaPeggioreInserimento_ARN/nMedia)
        tempiPerGraficoPeggioreRicerca_ARN.append(tSommaPerMediaPeggioreRicerca_ARN/nMedia)
        
        tempiPerGraficoInserimentoCasuale_ARN.append(tSommaPerMediaInserimentoCasuale_ARN/nMedia)
        tempiPerGraficoRicercaCasuale_ARN.append(tSommaPerMediaRicercaCasuale_ARN/nMedia)
        tempiPerGraficoAttraversamentoCasuale_ARN.append(tSommaPerMediaAttraversamentoCasuale_ARN/nMedia)
        
        mediaAltezzaAlberoPeggiore_ABR.append(sommaPerMediaAltezzaAlberoPeggiore_ABR/nMedia) 
        mediaAltezzaAlberoCasuale_ABR.append(sommaPerMediaAltezzaAlberoCasuale_ABR/nMedia)

        mediaAltezzaAlberoPeggiore_ARN.append(sommaPerMediaAltezzaAlberoPeggiore_ARN/nMedia)
        mediaAltezzaAlberoCasuale_ARN.append(sommaPerMediaAltezzaAlberoCasuale_ARN/nMedia)
        
        if time.time() > timeMax:
            print("Il tempo massimo di esecuzione è stato superato")
            break
    
    #-----GRAFICI-----
    # GRAFICO (peggior inserimento ABR e ARN)
    plt.plot(range(1, len(tempiPerGraficoPeggioreInserimento_ABR) + 1), tempiPerGraficoPeggioreInserimento_ABR, 'g') #in verde ABR
    plt.plot(range(1, len(tempiPerGraficoPeggioreInserimento_ARN) + 1), tempiPerGraficoPeggioreInserimento_ARN, 'r') #in rosso ARN
    plt.xlabel("n")
    plt.ylabel("tempo (s)")
    plt.title("Inserimento, peggiore ABR in verde e ARN in rosso")
    plt.show()
    
    # GRAFICO (peggior ricerca ABR e ARN)
    plt.plot(range(1, len(tempiPerGraficoPeggioreRicerca_ABR) + 1), tempiPerGraficoPeggioreRicerca_ABR, 'g')
    plt.plot(range(1, len(tempiPerGraficoPeggioreRicerca_ARN) + 1), tempiPerGraficoPeggioreRicerca_ARN, 'r')
    plt.xlabel("n")
    plt.ylabel("tempo (s)")
    plt.title("Ricerca, peggiore ABR in verde e ARN in rosso")
    plt.show()
    
    # GRAFICO (inserimento casuale ABR e ARN)
    plt.plot(range(1, len(tempiPerGraficoInserimentoCasuale_ABR) + 1), tempiPerGraficoInserimentoCasuale_ABR, 'g')
    plt.plot(range(1, len(tempiPerGraficoInserimentoCasuale_ARN) + 1), tempiPerGraficoInserimentoCasuale_ARN, 'r')
    plt.xlabel("n")
    plt.ylabel("tempo (s)")
    plt.title("Inserimento, casuale ABR in verde e ARN in rosso")
    plt.show()
    
    # GRAFICO (ricerca casuale ABR e ARN)
    plt.plot(range(1, len(tempiPerGraficoRicercaCasuale_ABR) + 1), tempiPerGraficoRicercaCasuale_ABR, 'g')
    plt.plot(range(1, len(tempiPerGraficoRicercaCasuale_ARN) + 1), tempiPerGraficoRicercaCasuale_ARN, 'r')
    plt.xlabel("n")
    plt.ylabel("tempo (s)")
    plt.title("Ricerca, casuale ABR in verde e ARN in rosso")
    plt.show()
    
    # GRAFICO (attraversamento ABR e ARN)
    plt.plot(range(1, len(tempiPerGraficoAttraversamentoCasuale_ABR) + 1), tempiPerGraficoAttraversamentoCasuale_ABR, 'g')
    plt.plot(range(1, len(tempiPerGraficoAttraversamentoCasuale_ARN) + 1), tempiPerGraficoAttraversamentoCasuale_ARN, 'r')
    plt.xlabel("n")
    plt.ylabel("tempo (s)")
    plt.title("Attraversamento, ABR in verde e ARN in rosso")
    plt.show()
    
    
    #-----TABELLE-----
    #per creare la tabella non si prendono tutti i tempi da 1 a nMax, ma si prendono solo i tempi con uno step di 100 in 100 fino a nMax
    step = 100 #si procede di 100 fino ad arrivare a nMax valori da ordinare

    nValue = [] #serve alla tabella per indicare il numero di valori a cui ci riferiamo con un determinato tempo
    for k in range(0, nMax, step):
        nValue.append(k)
    nValue.append(i)
    
    altezzaAlberoPeggiore_ABR = [] #serve alla tabella per indicare l'altezza dell'albero ABR peggiore
    for k in range(0, len(mediaAltezzaAlberoPeggiore_ABR), step):
        altezzaAlberoPeggiore_ABR.append(round(mediaAltezzaAlberoPeggiore_ABR[k], 0)) #round approssima a 0 cifre dopo la virgola 
    altezzaAlberoPeggiore_ABR.append(round(mediaAltezzaAlberoPeggiore_ABR[i - 1], 0)) #serve per prendere anche l'ultimo valore
    
    altezzaAlberoPeggiore_ARN = [] #serve alla tabella per indicare l'altezza dell'albero ARN peggiore
    for k in range(0, len(mediaAltezzaAlberoPeggiore_ARN), step):
        altezzaAlberoPeggiore_ARN.append(round(mediaAltezzaAlberoPeggiore_ARN[k], 0)) #round approssima a 0 cifre dopo la virgola 
    altezzaAlberoPeggiore_ARN.append(round(mediaAltezzaAlberoPeggiore_ARN[i - 1], 0)) #serve per prendere anche l'ultimo valore
    
    altezzaAlberoCasuale_ABR = [] #serve alla tabella per indicare l'altezza dell'albero ABR casuale
    for k in range(0, len(mediaAltezzaAlberoCasuale_ABR), step):
        altezzaAlberoCasuale_ABR.append(round(mediaAltezzaAlberoCasuale_ABR[k], 0)) #round approssima a 0 cifre dopo la virgola 
    altezzaAlberoCasuale_ABR.append(round(mediaAltezzaAlberoCasuale_ABR[i - 1], 0)) #serve per prendere anche l'ultimo valore
    
    altezzaAlberoCasuale_ARN = [] #serve alla tabella per indicare l'altezza dell'albero ABR casuale
    for k in range(0, len(mediaAltezzaAlberoCasuale_ARN), step):
        altezzaAlberoCasuale_ARN.append(round(mediaAltezzaAlberoCasuale_ARN[k], 0)) #round approssima a 1 cifre dopo la virgola 
    altezzaAlberoCasuale_ARN.append(round(mediaAltezzaAlberoCasuale_ARN[i - 1], 0)) #serve per prendere anche l'ultimo valore
    
    # TABELLA (peggior inserimento ABR e ARN)
    tPeggioreInserimento_ABR = [] #serve alla tabella per indicare il tempo del calcolo di inserimento ABR (peggiore) con un determinato tempo
    for k in range(0, len(tempiPerGraficoPeggioreInserimento_ABR), step):
        tPeggioreInserimento_ABR.append(round(tempiPerGraficoPeggioreInserimento_ABR[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tPeggioreInserimento_ABR.append(round(tempiPerGraficoPeggioreInserimento_ABR[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    tPeggioreInserimento_ARN = [] #serve alla tabella per indicare il tempo del calcolo di inserimento ARN (peggiore) con un determinato tempo
    for k in range(0, len(tempiPerGraficoPeggioreInserimento_ARN), step):
        tPeggioreInserimento_ARN.append(round(tempiPerGraficoPeggioreInserimento_ARN[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tPeggioreInserimento_ARN.append(round(tempiPerGraficoPeggioreInserimento_ARN[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    trace = go.Table(header=dict(values=['Numero di valori','Altezza ABR', 'Altezza ARN', 'Tempo peggiore inserimento ABR (ms)', 'Tempo peggiore inserimento ARN (ms)']),cells=dict(values=[nValue, altezzaAlberoPeggiore_ABR, altezzaAlberoPeggiore_ARN, tPeggioreInserimento_ABR, tPeggioreInserimento_ARN,])) #generazione tabella .html con libreria plotly
    data = [trace]
    py.offline.plot(data, filename='tabella_peggioreInserimento.html') #metodo plot serve per 'disegnare' la tabella
    
    
    # TABELLA (peggior ricerca ABR e ARN)
    tPeggioreRicerca_ABR = [] #serve alla tabella per indicare il tempo del calcolo di ricerca ABR (peggiore) con un determinato tempo
    for k in range(0, len(tempiPerGraficoPeggioreRicerca_ABR), step):
        tPeggioreRicerca_ABR.append(round(tempiPerGraficoPeggioreRicerca_ABR[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tPeggioreRicerca_ABR.append(round(tempiPerGraficoPeggioreRicerca_ABR[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    tPeggioreRicerca_ARN = [] #serve alla tabella per indicare il tempo del calcolo di ricerca ARN (peggiore) con un determinato tempo
    for k in range(0, len(tempiPerGraficoPeggioreRicerca_ARN), step):
        tPeggioreRicerca_ARN.append(round(tempiPerGraficoPeggioreRicerca_ARN[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tPeggioreRicerca_ARN.append(round(tempiPerGraficoPeggioreRicerca_ARN[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    trace = go.Table(header=dict(values=['Numero di valori','Altezza ABR', 'Altezza ARN', 'Tempo peggiore ricerca ABR (ms)', 'Tempo peggiore ricerca ARN (ms)']),cells=dict(values=[nValue, altezzaAlberoPeggiore_ABR, altezzaAlberoPeggiore_ARN, tPeggioreRicerca_ABR, tPeggioreRicerca_ARN,])) #generazione tabella .html con libreria plotly
    data = [trace]
    py.offline.plot(data, filename='tabella_peggioreRicerca.html') #metodo plot serve per 'disegnare' la tabella
    
    
    # TABELLA (inserimento casuale ABR e ARN)
    tInserimentoCasuale_ABR = [] #serve alla tabella per indicare il tempo del calcolo di inserimento ABR (casuale) con un determinato tempo
    for k in range(0, len(tempiPerGraficoInserimentoCasuale_ABR), step):
        tInserimentoCasuale_ABR.append(round(tempiPerGraficoInserimentoCasuale_ABR[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tInserimentoCasuale_ABR.append(round(tempiPerGraficoInserimentoCasuale_ABR[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    tInserimentoCasuale_ARN = [] #serve alla tabella per indicare il tempo del calcolo di inserimento ARN (casuale) con un determinato tempo
    for k in range(0, len(tempiPerGraficoInserimentoCasuale_ARN), step):
        tInserimentoCasuale_ARN.append(round(tempiPerGraficoInserimentoCasuale_ARN[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tInserimentoCasuale_ARN.append(round(tempiPerGraficoInserimentoCasuale_ARN[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore

    trace = go.Table(header=dict(values=['Numero di valori', 'Altezza ABR', 'Altezza ARN', 'Tempo inserimento casuale ABR (ms)', 'Tempo inserimento casuale ARN (ms)']),cells=dict(values=[nValue, altezzaAlberoCasuale_ABR, altezzaAlberoCasuale_ARN, tInserimentoCasuale_ABR, tInserimentoCasuale_ARN,])) #generazione tabella .html con libreria plotly
    data = [trace]
    py.offline.plot(data, filename='tabella_inserimentoCasuale.html') #metodo plot serve per 'disegnare' la tabella
    
    
    # TABELLA (ricerca casuale ABR e ARN)
    tRicercaCasuale_ABR = [] #serve alla tabella per indicare il tempo del calcolo di ricerca ABR (casuale) con un determinato tempo
    for k in range(0, len(tempiPerGraficoRicercaCasuale_ABR), step):
        tRicercaCasuale_ABR.append(round(tempiPerGraficoRicercaCasuale_ABR[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tRicercaCasuale_ABR.append(round(tempiPerGraficoRicercaCasuale_ABR[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    tRicercaCasuale_ARN = [] #serve alla tabella per indicare il tempo del calcolo di ricerca ARN (casuale) con un determinato tempo
    for k in range(0, len(tempiPerGraficoRicercaCasuale_ARN), step):
        tRicercaCasuale_ARN.append(round(tempiPerGraficoRicercaCasuale_ARN[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tRicercaCasuale_ARN.append(round(tempiPerGraficoRicercaCasuale_ARN[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore

    trace = go.Table(header=dict(values=['Numero di valori', 'Altezza ABR', 'Altezza ARN', 'Tempo ricerca casuale ABR (ms)', 'Tempo ricerca casuale ARN (ms)']),cells=dict(values=[nValue, altezzaAlberoCasuale_ABR, altezzaAlberoCasuale_ARN, tRicercaCasuale_ABR, tRicercaCasuale_ARN,])) #generazione tabella .html con libreria plotly
    data = [trace]
    py.offline.plot(data, filename='tabella_ricercaCasuale.html') #metodo plot serve per 'disegnare' la tabella
    
    
    # TABELLA (attraversamento ABR e ARN)
    tAttraversamento_ABR = [] #serve alla tabella per indicare il tempo del calcolo di attraversamento ABR (casuale) con un determinato tempo
    for k in range(0, len(tempiPerGraficoAttraversamentoCasuale_ABR), step):
        tAttraversamento_ABR.append(round(tempiPerGraficoAttraversamentoCasuale_ABR[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tAttraversamento_ABR.append(round(tempiPerGraficoAttraversamentoCasuale_ABR[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    tAttraversamento_ARN = [] #serve alla tabella per indicare il tempo del calcolo di attraversamento ARN (casuale) con un determinato tempo
    for k in range(0, len(tempiPerGraficoAttraversamentoCasuale_ARN), step):
        tAttraversamento_ARN.append(round(tempiPerGraficoAttraversamentoCasuale_ARN[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tAttraversamento_ARN.append(round(tempiPerGraficoAttraversamentoCasuale_ARN[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore

    trace = go.Table(header=dict(values=['Numero di valori', 'Altezza ABR', 'Altezza ARN', 'Tempo attraversamento ABR (ms)', 'Tempo attraversamento ARN (ms)']),cells=dict(values=[nValue, altezzaAlberoCasuale_ABR, altezzaAlberoCasuale_ARN, tAttraversamento_ABR, tAttraversamento_ARN,])) #generazione tabella .html con libreria plotly
    data = [trace]
    py.offline.plot(data, filename='tabella_attraversamento.html') #metodo plot serve per 'disegnare' la tabella
    
    
