from timeit import default_timer as timer
import time
import random

#array cASUale 
def casualArray(numValues, rangeValues):
    #print("Array casuale composto da", numValues,"elementi che hanno valore da 0 a", rangeValues)
    myArray = []
    for i in range(numValues):
        newValue = random.randrange(0, rangeValues) #crea un numero casuale da 0 a rangeValues
        myArray.append(newValue)
    #print("Array è:")
    #print(myArray) #è il print per vedere quale array viene generato
    return myArray

#array già ordinato
def orderedArray(numValues, rangeValues):
    #print("Array casuale composto da", numValues,"elementi che hanno valore da 0 a", rangeValues)
    myArray = []
    for i in range(numValues):
        newValue = i 
        myArray.append(newValue)
    #print("Array è:")
    #print(myArray) #è il print per vedere quale array viene generato
    return myArray

#array ordinato al contrario
def reverseOrderedArray(numValues, rangeValues):
    #print("Array casuale composto da", numValues,"elementi che hanno valore da 0 a", rangeValues)
    myArray = []
    for i in range(numValues):
        newValue = numValues + 1 - i 
        myArray.append(newValue)
    #print("Array è:")
    #print(myArray) #è il print per vedere quale array viene generato
    return myArray

#array cAUSale (scelto)
def causalArray():
    myArray = [182, 566, 270, 265, 970, 502, 393, 633, 70, 39]
    print("Array è:")
    print(myArray)
    return myArray

#InsertionSort iterativo
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1        
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

#Funzione Quick sort 
#A[]-->l'Array che deve essere ordinato, low-->l'indice di partenza, high-->l'indice finale
def quickSort(A, low, high):
    if len(A) == 1: #se l'array è lungo 1 vuol dire che è già ordinato
        return A
    if low < high: 
        #partitionIndex è il partizionamento degli indici, adesso A[p] è al posto giusto (ma i due sottoarray sono da ordinare)
        partitionIndex = partition(A, low, high)
            
        #Separatamente ordina gli elementi prima della partizione e dopo la partizione (in modo ricorsivo)
        quickSort(A, low, partitionIndex-1)
        quickSort(A, partitionIndex+1, high)
      
    
#Funzione Partition di Quicksort
def partition(A, low, high):
    i = (low-1) #indice degli elementi più piccoli
    pivot = A[high] #pivot (prende l'ultimo elemento dell'array)

    for j in range(low, high):
        #Se l'elemento corrente è più piccolo o uguale del pivot
        if A[j] <= pivot:
            #incrementa l'indice dell'elemento più piccolo
            i = i+1 #l'indice degli elementi più piccoli del pivot aumenta di uno
            A[i], A[j] = A[j], A[i] #Realizza uno Swap tra i valori A[i] e A[j]
            
    A[i+1], A[high] = A[high], A[i+1]  #Realizza uno Swap tra i valori A[i+1] e A[high] (metto il pivot nella posizione corretta)
    return (i+1) #ritorno il pivot