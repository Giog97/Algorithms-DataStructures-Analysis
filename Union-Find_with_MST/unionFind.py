#struttura dati Union-Find
#composto da: -un dizionario che contiene insiemi disgiunti; -un indice che serve quando inseriamo un nuovo valore, a dare una chiave (rappresentante) al'insieme;
#Nello specifico implementa 3 operazioni: -FindSet: determina in quale insieme si trova un particolare elemento, restiutendo la chiave dell'insieme;
#-Union: combina o fonde due insiemi in un unico insieme;
#-MakeSet: aggiunge singoli elementi al dizionario, come se fossero insiemi costituiti da 1 elemento.
class unionFind:
    S = {}  #insieme degli insiemi (dizionario che sono delle raccolte non ordinate di oggetti che presentano coppie composte da chiavi e valori).
    #esempio monete = {1:'euro',2:'dollaro',3:'sterlina'}
    index = 0  #indice (serve per dare un "nome" agli insiemi di S, ovvero alle sue chiavi ovvero i rappresentanti)

    #Costruttore
    def __init__(self):
        self.S = {}  #il dizionario è inizialmente vuoto
        self.index = 0  #l'indice è inizialmente nullo

    #Make set
    #crea un nuovo insieme il cui unico elemento è x e chiave è index. E lo inserisce nel dizionario S di UnionFind. In seguito incrementa l'indice (cioè la chiave)
    def makeSet(self, x):  #prende in ingresso un node x
        self.S[self.index] = [x]  #aggiunge un nuovo elemento con chiave index e valori x
        self.index = self.index + 1  #incrementa l'indice (in modo che alla prossima aggiunta l'indice sia già corretto)

    #Union
    #unisce gli insiemi che contengono x e y come valori, in un nuovo insieme che è l'unione di questi due insiemi.
    def union(self, x, y):  #unione tra x e y (valori appartenenti a qualche chiave in S)
        xKey = None  #bisogna innanzitutto cercare le chiavi di x e y tra quelle presenti nel dizionario S; inizialmente sono nulle (= sconosciute)
        yKey = None
        #scorro tutte le chiavi del dizionario, per ogni chiave scorro tra i suoi valori. Una volta trovato il valore = a x o y, prendo i valori delle chiavi che indicano l'insiemi da unire
        for k in self.S:  #ricerca per chiave (k)
            for value in self.S[k]:  #ricerca tra i valori nella chiave k
                if x == value:
                    xKey = k
                elif y == value:
                    yKey = k
        self.S[yKey] = self.S[yKey] + self.S[xKey]  #aggiunge i valori dell'insieme contenente x a quelli dell'insieme contenente y. La chiave (rappresentante) del nuovo insieme dato dall'unione sarà la chiave di y.
        self.S.pop(xKey)  #rimuove la chiave x dal dizionnario (perché va distrutta)

    #Find set
    #Restituisce la chiave k (rappresentate) dell'insieme che contiente x, se x esiste nel dizionario
    def findSet(self, x):
        for k in self.S:  #per ogni chiave k di S
            if x in self.S[k]:  #cerca tra i valori associati alla chiave k
                return k  #ritorna la chiave k dell'insieme cui x appartiene
        return None  #oppure ritorna None se x non esiste in S
