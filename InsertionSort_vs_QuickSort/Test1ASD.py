from timeit import default_timer as timer
import time
import random
import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go

import Es1ASD 

#Testa array già scelto = [182, 566, 270, 265, 970, 502, 393, 633, 70, 39]
def testGivenArray():
    givenArrayI = Es1ASD.causalArray()
    givenArrayQ = givenArrayI[:]

    #Testato il caso di array scelto per InsertionSort
    #parte il timer per contare i secondi che impiega a ordinare
    startInsertion = timer()       
    Es1ASD.insertionSort(givenArrayI)         
    print("\nArray ordinato con InsertionSort è:")
    print(givenArrayI) #printa l'array ordinato
    endInsertion = timer() #serve per fare la differenza con il tempo di partenza per sapere quanto ha impiegato
    print("\nIl tempo per eseguire InsertionSort è", endInsertion - startInsertion)
    
    #Testato il caso di array scelto per QuickSort
    #parte il timer per contare i secondi che impiega a ordinare
    startQuickSort = timer()         
    Es1ASD.quickSort(givenArrayQ, 0, len(givenArrayQ)-1)     
    print ("\nArray ordinato con QuickSort:")
    print (givenArrayQ) #printa l'array ordinato
    endQuickSort = timer() #serve per fare la differenza con il tempo di partenza per sapere quanto ha impiegato
    print("\nIl tempo per eseguire QuickSort è", endQuickSort - startQuickSort)
    
    
#test di InsertionSort e QuickSort nel caso medio per fare il grafico
def CasoMedio():
    nMax = 1000  #n° massimo di valori che verranno generati in un array da ordinare
    rangeValues = 1000; #è il valore max che gli elementi dell'array possono avere
    nMedia = 10 #è il numero di volte che calcoliamo il tempo di esecuzione per un certo numero di valori, per poter poi fare la media
    tMax = 1800  # tempo massimo consentito di esecuzione 30 min

    #array che servono per creare i grafici 
    tempoGraficoImedio = []  #tempi di esecuzione per InsertionSort nel caso medio
    tempoGraficoQmedio = []  #tempi di esecuzione per QuickSort nel caso medio
    
    for i in range(1, nMax):
        tempoSommaPerImedia = 0
        tempoSommaPerQmedia = 0
        for j in range(1, nMedia):
            arrayDaOrdinare = [] 
            arrayDaOrdinare = Es1ASD.casualArray(i, rangeValues)
            #arrayTestInsertionSort = Es1ASD.casualArray(i, rangeValues) #array casuale con i numeri con valori fino a rangeValues
            arrayTestInsertionSort = arrayDaOrdinare[:]
            arrayTestQuickSort = arrayDaOrdinare[:]

            #Calcolo il tempo con un timer sullo stesso array per InsertionSort e QuickSort
            #InsertionSort
            startInsertion = timer() #parte il timer per contare i secondi che impiega a ordinare
            Es1ASD.insertionSort(arrayTestInsertionSort)
            endInsertion = timer() #serve per fare la differenza con il tempo di partenza per sapere quanto ha impiegato
            #tempoSommaPerImedia = tempoSommaPerImedia + (endInsertion - startInsertion)
            tempoParzialeImedia = endInsertion - startInsertion
            tempoSommaPerImedia = tempoSommaPerImedia + tempoParzialeImedia

            #QuickSort
            startQuickSort = timer() #parte il timer per contare i secondi che impiega a ordinare
            Es1ASD.quickSort(arrayTestQuickSort, 0, i-1)
            endQuickSort = timer() #serve per fare la differenza con il tempo di partenza per sapere quanto ha impiegato
            tempoParzialeQmedia = endQuickSort - startQuickSort
            tempoSommaPerQmedia = tempoSommaPerQmedia + tempoParzialeQmedia
            
        tempoPerImedia = tempoSommaPerImedia/nMedia
        tempoPerQmedia = tempoSommaPerQmedia/nMedia
        tempoGraficoImedio.append(tempoPerImedia)
        tempoGraficoQmedio.append(tempoPerQmedia)
        if (tempoGraficoImedio[i - 1] > tMax) or (tempoGraficoQmedio[i - 1] > tMax):
            break
    
    #Grafico
    plt.plot(range(1, len(tempoGraficoImedio) + 1), tempoGraficoImedio, 'r') #Grafico InsertionSortMedio in rosso
    plt.plot(range(1, len(tempoGraficoQmedio) + 1), tempoGraficoQmedio, 'g') #Grafico QuikSortMedio in verde
    plt.xlabel("n")
    plt.ylabel("tempo (s)")
    plt.title("Caso medio di InsertionSort in rosso e QuickSort in verde")
    plt.show()
    
    #TABELLA
    #per creare la tabella non si prendono tutti i tempi da 1 a nMax, ma si prendono solo i tempi con uno step di 100 in 100 fino a nMax
    step = 100 #si procede di 100 fino ad arrivare a nMax valori da ordinare

    nValue = [] #serve alla tabella per indicare il numero di valori a cui ci riferiamo con un determinato tempo
    for k in range(0, nMax, step):
        nValue.append(k)
    nValue.append(i)

    tIMedio = [] #serve alla tabella per indicare il tempo del calcolo di InsertionSort (peggiore) con un determinato tempo
    for k in range(0, len(tempoGraficoImedio), step):
        tIMedio.append(round(tempoGraficoImedio[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola
    tIMedio.append(round(tempoGraficoImedio[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    tQMedio = []  #serve alla tabella per indicare il tempo del calcolo di QuickSort (peggiore) con un determinato tempo
    for k in range(0, len(tempoGraficoQmedio), step):
        tQMedio.append(round(tempoGraficoQmedio[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola
    tQMedio.append(round(tempoGraficoQmedio[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore

    #generazione tabella .html con libreria plotly
    trace = go.Table(header=dict(values=['Numero di valori', 'Tempo InsertionSort caso Medio (ms)', 'Tempo QuickSort caso Medio (ms)']),cells=dict(values=[nValue, tIMedio, tQMedio,]))
    data = [trace]
    py.offline.plot(data, filename='tabella_InsertionSorteQuickSortCasoMedio.html') #metodo plot serve per 'disegnare' la tabella
    


#test di InsertionSort e QuickSort nel caso peggiore per fare il grafico
def CasoPeggiore():
    nMax = 1000  #n° massimo di valori che verranno generati in un array da ordinare
    rangeValues = 1000; #è il valore max che gli elementi dell'array possono avere
    nMedia = 10 #è il numero di volte che calcoliamo il tempo di esecuzione per un certo numero di valori, per poter poi fare la media (se metto 5 è troppo per fare la media)
    tMax = 1800  # tempo massimo consentito di esecuzione 30 min

    #array che servono per creare i grafici 
    tempoGraficoIpeggiore = []  #tempi di esecuzione per InsertionSort nel caso peggiore
    tempoGraficoQpeggiore = []  #tempi di esecuzione per QuickSort nel caso peggiore
    
    for i in range(1, nMax):
        tempoSommaPerImedia = 0
        tempoSommaPerQmedia = 0    
        for j in range(1, nMedia):
            arrayTestInsertionSort = Es1ASD.reverseOrderedArray(i, rangeValues) #array ordinato al contrario con i numeri con valori fino a rangeValues
            arrayTestQuickSort = arrayTestInsertionSort[:]
            
            #Calcolo il tempo con un timer sullo stesso array per InsertionSort e QuickSort
            #InsertionSort
            startInsertion = timer() #parte il timer per contare i secondi che impiega a ordinare
            Es1ASD.insertionSort(arrayTestInsertionSort)
            endInsertion = timer() #serve per fare la differenza con il tempo di partenza per sapere quanto ha impiegato
            #tempoGraficoIpeggiore.append(endInsertion - startInsertion)
            tempoSommaPerImedia = tempoSommaPerImedia + (endInsertion - startInsertion)
            
            #QuickSort 
            startQuickSort = timer() #parte il timer per contare i secondi che impiega a ordinare
            Es1ASD.quickSort(arrayTestQuickSort, 0, i-1)
            endQuickSort = timer() #serve per fare la differenza con il tempo di partenza per sapere quanto ha impiegato
            #tempoGraficoQpeggiore.append(endInsertion - startInsertion)
            tempoSommaPerQmedia = tempoSommaPerQmedia + (endQuickSort - startQuickSort)


        tempoGraficoIpeggiore.append(tempoSommaPerImedia/nMedia)
        tempoGraficoQpeggiore.append(tempoSommaPerQmedia/nMedia)
        if (tempoGraficoIpeggiore[i - 1] > tMax) or (tempoGraficoQpeggiore[i - 1] > tMax):
            break
    
    #GRAFICO
    plt.plot(range(1, len(tempoGraficoIpeggiore) + 1), tempoGraficoIpeggiore, 'r') #Grafico InsertionSortPeggiore in rosso
    plt.plot(range(1, len(tempoGraficoQpeggiore) + 1), tempoGraficoQpeggiore, 'g') #Grafico QucikSortPeggiore in verde
    plt.xlabel("n")
    plt.ylabel("tempo (s)")
    plt.title("Caso peggiore di InsertionSort in rosso e QuickSort in verde")
    plt.show()
    
    #TABELLA
    #per creare la tabella non si prendono tutti i tempi da 1 a nMax, ma si prendono solo i tempi con uno step di 100 in 100 fino a nMax
    step = 100 #si procede di 100 fino ad arrivare a nMax valori da ordinare

    nValue = [] #serve alla tabella per indicare il numero di valori a cui ci riferiamo con un determinato tempo
    for k in range(0, nMax, step):
        nValue.append(k)
    nValue.append(i)

    tIPeggiore = [] #serve alla tabella per indicare il tempo del calcolo di InsertionSort (peggiore) con un determinato tempo
    for k in range(0, len(tempoGraficoIpeggiore), step):
        tIPeggiore.append(round(tempoGraficoIpeggiore[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tIPeggiore.append(round(tempoGraficoIpeggiore[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore
    
    tQPeggiore = []  #serve alla tabella per indicare il tempo del calcolo di QuickSort (peggiore) con un determinato tempo
    for k in range(0, len(tempoGraficoQpeggiore), step):
        tQPeggiore.append(round(tempoGraficoQpeggiore[k]*1000, 5)) #round approssima a 5 cifre dopo la virgola (e moltiplicato per 10^5)
    tQPeggiore.append(round(tempoGraficoQpeggiore[i - 1]*1000, 5)) #serve per prendere anche l'ultimo valore

    #generazione tabella .html con libreria plotly
    trace = go.Table(header=dict(values=['Numero di valori', 'Tempo InsertionSort caso Peggiore (ms)', 'Tempo QuickSort caso Peggiore (ms)']),cells=dict(values=[nValue, tIPeggiore, tQPeggiore,]))
    data = [trace]
    py.offline.plot(data, filename='tabella_InsertionSorteQuickSortCasoPeggiore.html') #metodo plot serve per 'disegnare' la tabella



#test di InsertionSort nel caso migliore per fare il grafico
def InsertionSortMigliore():
    nMax = 1000  #n° massimo di valori che verranno generati in un array da ordinare
    rangeValues = 1000; #è il valore max che gli elementi dell'array possono avere
    nMedia = 15 #è il numero di volte che calcoliamo il tempo di esecuzione per un certo numero di valori, per poter poi fare la media
    tMax = 1800  # tempo massimo consentito di esecuzione 30 min

    #array che servono per creare i grafici 
    tempoGraficoImigliore = []  #tempi di esecuzione per InsertionSort nel caso migliore
    
    for i in range(1, nMax):
        tempoSommaPerImedia = 0
        tempoSommaPerQmedia = 0 
        for j in range(1, nMedia):
            arrayTestInsertionSort = Es1ASD.orderedArray(i, rangeValues) #array ordinato con i numeri con valori fino a rangeValues
            
            startInsertion = timer() #parte il timer per contare i secondi che impiega a ordinare
            Es1ASD.insertionSort(arrayTestInsertionSort)
            endInsertion = timer() #serve per fare la differenza con il tempo di partenza per sapere quanto ha impiegato
            #tempoGraficoImigliore.append(endInsertion - startInsertion)
            tempoSommaPerImedia = tempoSommaPerImedia + (endInsertion - startInsertion)
        tempoGraficoImigliore.append(tempoSommaPerImedia/nMedia)
        if (tempoGraficoImigliore[i - 1] > tMax):
            break
    
    #GRAFICO
    plt.plot(range(1, len(tempoGraficoImigliore) + 1), tempoGraficoImigliore, 'r') #Grafico InsertionSortMigliore in rosso
    plt.xlabel("n")
    plt.ylabel("tempo (s)")
    plt.title("InsertionSort, caso migliore")
    plt.show()
    
    #TABELLA
    #per creare la tabella non si prendono tutti i tempi da 1 a nMax, ma si prendono solo i tempi con uno step di 100 in 100 fino a nMax
    step = 100 #si procede di 100 fino ad arrivare a nMax valori da ordinare

    nValue = [] #serve alla tabella per indicare il numero di valori a cui ci riferiamo con un determinato tempo
    for k in range(0, nMax, step):
        nValue.append(k)
    nValue.append(i)

    tIMigliore = [] #serve alla tabella per indicare il tempo del calcolo di InsertionSort (migliore) con un determinato tempo
    for k in range(0, len(tempoGraficoImigliore), step):
        tIMigliore.append(round(tempoGraficoImigliore[k]* 1000, 5)) #round approssima a 3 cifre dopo la virgola (e moltiplicato per 10^5)
    tIMigliore.append(round(tempoGraficoImigliore[i - 1]* 1000, 5)) #serve per prendere anche l'ultimo valore

    #generazione tabella .html con libreria plotly
    trace = go.Table(header=dict(values=['Numero di valori', 'Tempo InsertionSort caso Migliore (ms)']),cells=dict(values=[nValue, tIMigliore,]))
    data = [trace]
    py.offline.plot(data, filename='tabella_InsertionSortCasoMigliore.html') #metodo plot serve per 'disegnare' la tabella

    