# GENERATORI
# = funzione speciale che ritorna un lazy iterator
# == oggetto che può essere iterato,
# ma che esegue operazioni necessarie a generare l' elemento successivo dell'iterabile
# SOLO al momento della chiamata
# sono utili quando:
# - è necessario mantenere lo stato di una funzione, senza costruire un oggetto/classe specifico
# - non si vuole occupare memoria per costruire in anticipo l'oggetto
# - si vuole generare gli oggetti (lazy) solo al momento dell'utilizzo

# si costruisce come una funzione, ma il risulltato viene tornato con yield al posto che con return
# DIFFERENZA:
# return: indica il punto in cui la funzione torna un risultato e termina l'esecuzione
# yield: indica il punto in cui la funzione torna un risultato
#        e si mette in pausa la funzione nella attuale configurazione

# generatore di 3 numeri
def generatore():
    # alla prima chiamata parte da qui
    print("primo")
    yield 101
    # alla seconda chiamata parte da qui
    print("secondo")
    yield 202
    # alla terza chiamata parte da qui
    print("terzo")
    yield 303
    # finisce il generatoe
# si utilizza definendo un oggetto generatore
g = generatore()
# e si chiama next() come ogni iteratore
next(g)
next(g)
next(g)
#next(g)     # quando finisce ritorna una StopIteration

# si può costruire anche un generatore 'infinito'
def pari():
    n=0
    while(True):
        yield n*2
        n = n + 1
p = pari()
print(next(p))
print(next(p))
print(next(p))



# altra differenza tra return e yield:
# dopo return non vengono più eseguite azioni, dopo yeld sì, alla chiamata successiva

# generatore compatto

# list comprehension:
valori = [1,2,3,4,5]
numeri_quadrati = [x*x for x in valori]
for v in numeri_quadrati:
    print(v)

# NON esistono tuple comprehension!!
valori = [1,2,3,4,5]
numeri_quadrati_g = ( x*x for x in valori)
type(numeri_quadrati_g)
# non è una tuple comprehension, bensì un generatore scritto in modo compatto
# infatti, se ne stampo il tipo:
print(type(numeri_quadrati))
print(type(numeri_quadrati_g))

# LAMBDA FUNCTIONS
# = funzioni anonime che permettono di introdurre un nuovo scopo locale
# alla funzione che può essere definita e usata nella stessa linea di codice.
# Le lambda functions possono vedere tutte le variabili che esistono nello scope in cui lambda è creata.
# Possono avere un numero qualsiasi di variabili, ma una sola espressione:
x = lambda a : a + 7
print(x(5))     # 12
# sommo due numeri
x = lambda a,b : a + b
print( x(5,3) )     # 8
# alla creazione, una lambda function non fa nessuna copia delle variabili che "vivono" nello stesso scopo in cui è creata,
# ma mantiene un riferimento per "vederle"
# utile quando si vogliono svolgere azioni ripetitive localmente,
# senza dover definire un'intera funzione per svolgerle e quindi scrivere molto codice.

# TIP: Una lambda function contiene in genere le operazioni che si possono mettere nella istruzione return di una funzione













