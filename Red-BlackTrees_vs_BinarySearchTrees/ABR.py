#NODO
#è la struttura dati che rappresenta il nodo di un albero binario
class NodoABR:
    def __init__(self, key): #attributi
        self.key = key #chiave
        self.p = None #padre
        self.left = None #figlio sx
        self.right = None #figlio dx

#ABR
#è la struttura dati che rappresenta l'albero binario
class ABR:
    def __init__(self): #inizializzo mettendo una radice nulla
        self.root = None #albero vuoto

    #INSERT
    #è l'inserimento in un albero binario fatto in modo iterativo.
    def insert(self, z):
        #puntatori che devono essere aggiornati duranti l'iterazione
        y = None #puntatore al padre
        x = self.root #puntatore al nodo attuale. Serve per trovare la corretta posizione. Si parte dalla radice.
        while x is not None: #finchè x non punta a una foglia, quindi il suo valore è nullo si itera.
            y = x #il nuovo puntatore a padre y sarà il vecchio valore del puntatore x
            if z.key < x.key: #se il valore che vogliamo inserire z, è minore del valore del nodo corrente x, allora si procede a cercare una foglia nel sottoalbero sinistro. Altrimenti si va nel sottoalbero destro
                x = x.left
            else:
                x = x.right
        z.p = y #il padre del nuovo nodo, sarà il nodo puntato da y
        if y is None: #se y è nullo vuol dire che ho introdotto il 1° elemento dell'albero e quindi il nuovo valore diventa la radice del mio albero
            self.root = z
        elif z.key < y.key: #se il valore di z è minore del valore del valore di suo padre y, allora sarà un figlio sinistro (y.left). Se invece è maggiore, allora sarà un figlio destro (y.right)
            y.left = z
        else:
            y.right = z
        #il nuovo nodo avrà i puntatori ai suoi due figli (dx e sx) nulli, perchè sono due nuove foglie.
        z.left = None
        z.right = None

    #SEARCH
    #è una ricerca binaria iterativa. Restituisce vero se l'elemento è presente e falso se non lo è
    def search(self, key):
        x = self.root #puntatore al nodo per vedere se il valore cercato è nell'albero. Si parte dalla radice.
        while x is not None and key != x.key: #finchè non trovo il valore cercato o non ho x nullo, itero
            if key < x.key: #se il valore che cerchiamo è minore del valore nel nodo corrente allora continuo nel sottoalbero sinistro se è maggiore continuo nel sottoalbero destro.
                x = x.left
            else:
                x = x.right
        #Se x cioè il puntatore che stava scorrendo per trovare il valore è nullo vuol dire che sono arrivato in fondo all'albero e non ho trovato il valore quindi restituisco False.
        #In caso contrario ho trovato il valore e allora restituisco True
        if x is None:
            return False
        else:
            return True

    #INORDER TREE WALK
    #è l'attraversamento simmetrico ricorsivo. Elenca ordinatamente tutte le chiavi dell'albero
    def inorder(self):
        def _inorder(x):
            if(x is None): #se x è una foglia/vuoto torna indietro/termina
                return
            if(x.left != None): #va a sinistra se il sottoalbero sx non è vuoto
                _inorder(x.left)
            # print(x.key) #stampa la chiave
            if(x.right != None): #va a destra se il sottoalbero dx non è vuoto
                _inorder(x.right)
                
        #per attraversare tutto l'albero devo passare la radice alla funzione _inorder() che è definita sopra
        _inorder(self.root)
    
    #HEIGHT
    #è l'altezza di ABR
    def height(self):
        def _height(x):
            if (x is None): 
                return -1
            altezzaSx = _height(x.left) #va nel sottoalbero a sinistra
            altezzaDx = _height(x.right) #va nel sottoalbero a destra
            return 1+max(altezzaSx, altezzaDx) #ogni volta ritorna l'altezza = 1 + max altezza dei figli
        #per attraversare tutto l'albero devo passare la radice alla funzione _inorder() che è definita sopra
        return _height(self.root)

