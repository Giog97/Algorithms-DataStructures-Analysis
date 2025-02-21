#NODO
#è la struttura dati che rappresenta il nodo di un albero rosso-nero
class NodoARN:
    def __init__(self, key): #attributi
        self.key = key #chiave
        self.p = None #padre
        self.left = None #figlio sx
        self.right = None #figlio dx
        self.color = False #colore (False=Nero, True=Rosso)
        #mettere il colore server per rendere l'albero binario più bilanciato

#ARN
#è la struttura dati che rappresenta l'albero binario. Usato T.nil come sentinella che rappresenta NIL. In particolare il suo color è Nero(=False). Così facendo le condizioni al contorno sono semplificate.
class ARN:
    def __init__(self): #inizializzo mettendo un nodo con valore nullo
        self.nil = NodoARN(None) #T.nil rappresenta la sentinella.
        self.root = self.nil #albero vuoto

    #INSERT
    #è l'inserimento in un ARN fatto in modo iterativo.
    def insert(self, z):
        #puntatori che devono essere aggiornati duranti l'iterazione
        y = self.nil #puntatore al padre
        x = self.root #puntatore al nodo attual. Serve per trovare la corretta posizione. Si parte dalla radice.
        while x != self.nil: #finchè x non punta alla sentinella nil (foglia)
            y = x #il nuovo puntatore a padre y sarà il vecchio valore del puntatore x
            if z.key < x.key: #se il valore che vogliamo inserire z, è minore del valore del nodo corrente x, allora si procede a cercare una foglia nel sottoalbero sinistro. Altrimenti si va nel sottoalbero destro
                x = x.left
            else:
                x = x.right
        z.p = y #il padre del nuovo nodo, sarà il nodo puntato da y
        if y == self.nil: #se y è nil vuol dire che ho introdotto il 1° elemento dell'albero e quindi il nuovo valore diventa la radice del mio albero
            self.root = z
        elif z.key < y.key: #se il valore di z è minore del valore del valore di suo padre y, allora sarà un figlio sinistro (y.left). Se invece è maggiore, allora sarà un figlio destro (y.right)
            y.left = z
        else:
            y.right = z
        #il nuovo nodo avrà i puntatori ai suoi due figli (dx e sx) nil, perchè sono due nuove foglie.
        z.left = self.nil
        z.right = self.nil
        z.color = True #imposto il colore del nuovo nodo come Rosso (=true), ciò potrebbe violare alcune proprità di ARN (radice nera, nodo rosso non può avere figlio rosso)
        self.insertFixup(z) #chiamo la funzione ausiliaria insertFixup per ricolorare i nodi ed effettuare le rotazioni necessarie per preservare le proprietà ARN

    #INSERT FIXUP
    #è una procedura ausiliaria che ricolora i nodi ed effettua delle rotazioni, in pratica ripristina le proprietà di ARN
    #color -> True=Rosso, False=Nero
    def insertFixup(self, z):
        while z.p.color == True: 
            if z.p == z.p.p.left: #se il padre di z è figlio sinistro del nonno di z
                y = z.p.p.right #y prende il valore dello zio di z (cioè l'altro figlio del nonno)
                if y.color == True: #CASO 1: lo zio y di z è rosso
                    z.p.color = False #coloro di nero il padre di z
                    y.color = False #coloro di nero lo zio di z
                    z.p.p.color = True #coloro di rosso il nonno z
                    z = z.p.p #ripeto il ciclo while con il nonno di z come nuovo z 
                else:
                    if z == z.p.right: #CASO 2: lo zio y di z è nero e z è un figlio destro
                        z = z.p #sposto z al suo padre (sono entrambi rossi). L'identità del nonno rimane invariata perchè dopo faccio un left rotate
                        self.leftRotate(z) #effettuo una rotazione sinistra per riportarmi nel Caso3
                    #CASO 3: lo zio y di z è nero e z è un figlio sinistro
                    z.p.color = False #coloro il padre di z di nero. Dopo il ciclo while non verrà eseguito un'altra volta perchè z.p ora è nero (False)
                    z.p.p.color = True #coloro il nonno di z di rosso
                    self.rightRotate(z.p.p) #effettuo una rotazione destra che sistema le cose 
            else: #come la clausola if ma con "right" e "left" scambiati
                #il padre di z è figlio destro del nonno di z
                y = z.p.p.left
                if y.color == True:
                    z.p.color = False
                    y.color = False
                    z.p.p.color = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = False
                    z.p.p.color = True
                    self.leftRotate(z.p.p)
        self.root.color = False #imposto il colore della radice a nero per mantenere le proprietà di ARN

    #LEFT ROTATE
    #Serve per ripristinare le proprietà di ARN dopo un inserimento. Per essere applicato il nodo x deve avere figlio destro y diverso da T.nil.
    #Nello specifio il nodo y diventa la nuova radice del sottoalbero, con x come figlio sinistro di y e il figlio sinistro di y come figlio destro di x
    def leftRotate(self, x):
        y = x.right #y diventa il figlio destro di x
        x.right = y.left #il figlio destro di x diventa il figlio sinistro di y. Sposta così il sottoalbero sinistro di y nel sottoalbero destro di x
        if y.left != self.nil: #se il figlio sinistro di y non è una foglia
            y.left.p = x #il padre del figlio sinistro di y diventa x
        y.p = x.p #collego il padre cioè il padre di y diventa il padre di x
        if x.p == self.nil: #se il padre di x è uguale alla sentinella, vuol dire che x era la radice
            self.root = y #y diventa la nuova radice
        elif x == x.p.left: #se x è figlio sinistro del padre
            x.p.left = y #y diventa il nuovo figlio sinistro del padre di x
        else: #se x è figlio destro del padre
            x.p.right = y #y diventa il nuovo figlio destro del padre
        y.left = x #x diventa il figlio sinistro di y
        x.p = y #y diventa padre di x

    #RIGHT ROTATE
    #Serve per ripristinare le proprietà di ARN dopo un inserimento. Per essere applicato il nodo x deve avere figlio sinistro y diverso da T.nil.
    #Nello specifio il nodo y diventa la nuova radice del sottoalbero, con x come figlio destro di y e il figlio destro di y come figlio destro di x
    def rightRotate(self, x):
        y = x.left #y diventa il figlio sinistro di x
        x.left = y.right #il figlio sinistro di x diventa il figlio destro di y. Sposta così il sottoalbero destro di y nel sottoalbero sinistro di x
        if y.right != self.nil: #se il figlio dx di y non è una foglia
            y.right.p = x #il padre del figlio dx di y diventa x
        y.p = x.p #collego il padre cioè il padre di y diventa il padre di x
        if x.p == self.nil: #se il padre di x è uguale alla sentinella, vuol dire che x era la radice
            self.root = y #y diventa la nuova radice
        elif x == x.p.right: #se x è figlio dx del padre
            x.p.right = y #y diventa il nuovo figlio dx del padre di x
        else: #se x è figlio sx del padre
            x.p.left = y #y diventa il nuovo figlio sx del padre
        y.right = x #x diventa il figlio dx di y
        x.p = y #y diventa padre di x

    #SEARCH
    #è una ricerca binaria iterativa. Restituisce vero se l'elemento è presente e falso se non lo è
    def search(self, key):
        x = self.root #puntatore al nodo per vedere se il valore cercato è nell'albero. Si parte dalla radice.
        while x != self.nil and key != x.key: #finchè non trovo il valore cercato o non ho x nullo, itero
            if key < x.key: #se il valore che cerchiamo è minore del valore nel nodo corrente allora continuo nel sottoalbero sinistro se è maggiore continuo nel sottoalbero destro.
                x = x.left
            else:
                x = x.right
        #Se x cioè il puntatore che stava scorrendo per trovare il valore è nullo vuol dire che sono arrivato in fondo all'albero e non ho trovato il valore quindi restituisco False.
        #In caso contrario ho trovato il valore e allora restituisco True
        if x == self.nil:
            return False
        else:
            return True

    #INORDER TREE WALK
    #è l'attraversamento simmetrico ricorsivo. Elenca ordinatamente tutte le chiavi dell'albero
    def inorder(self):
        def _inorder(x):
            if(x == self.nil): #se x è una foglia torna indietro/termina
                return
            if(x.left != None): # va a sinistra se il sottoalbero sx non è vuoto
                _inorder(x.left)
            # print(x.key) # stampa la chiave
            if(x.right != None): # va a destra se il sottoalbero dx non è vuoto
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
