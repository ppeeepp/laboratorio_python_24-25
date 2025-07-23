# UNPACKING, GENERATORI, LAMBDA

# UNPACKING
# consente di assegnare un oggetto iterabile contenente dei valori ad un oggetto iterabile di variabili
# operazione opposta: PACKING, come nella creazione di una tupla
values = (1, 2, 3)
a, b, c = values
print(a)        # 1
print(b)        # 2
print(c)        # 3
# operatore *
# = UNPACKING OPERATOR -> permette di estendere la funzionalità dell'operazine di unpacking
# per impacchettare o spacchettare più valori in un'operazione
*b, = 1, 2      # L’oggetto a cui viene assegnata la tupla di valori deve essere una tupla.
                # Quindi la , è importante!
print(b)        # [1, 2]
# si può anche scegliere quali variabili spacchettare
a, *b = 1, 2, 3
print(a)        # 1
print(b)        # [2, 3]
# dopo aver obbligatoriamente riempito la variabile a, il resto viene assegnato a b

# il packing di più valori in un'unica variabile vale per raggruppare i valori
# inizio:
*a, b, c = 1, 2, 3, 4
# fine:
d, e, *f = 5, 6, 7, 8
# in mezzo:
g, *h, i = 9, 10, 11, 12

# la variabile usata come iterabile e riempita con l'operatore di unpacking può rimanere anche vuota
*pluto, pippo, paperino = 1, 2
print(pluto)    # []
print(pippo)    # 1
print(paperino) # 2

# NON può esserci un operatore di unpacking nella stessa operazione!
'''*a, *b = 1, 2, 3, 4
print(a)
print(b)
'''
# unione di liste
a = [1, 2]
b = [3, 4]
c = [a, b]
print(c)        # [[1, 2], [3, 4]] <-- lista annidata: lista di liste
# unione dei VALORI di due liste
a = [1, 2]
b = [3, 4]
c = [*a, *b]
print(c)        # [1, 2, 3, 4]

# UNPACKING DI DIZIONARI
# ** = DICTIONARY UNPACKING OPERATOR
# utile a spacchettare i valori contenuti in un dizionario o poter unire due dizionari
a = {'uno':1, 'due':2}
b = {'tre':3, 'quattro':4}
c = {**a, **b}
print(c)        # {'uno': 1, 'due': 2, 'tre': 3, 'quattro': 4}

# si possono utilizzare gli operatori * e **
# per definire come trattare la struttura iterabile chiave-valore
d = {'a':1, 'b':2}

def f(a, b):
    print(a)
    print(b)
f(*d)   # per le CHIAVI
f(**d)  # per i VALORI

# UNPACKING E FUNZIONI
def func (a, b):
  print(a)
  print(b)
# i parametri possono essere passati in modo posizionale
# = nell'ordine in cui si vuole riempire i parametri della funzione
func(2, 1)
# e come KEYWORD = ad ogni parametro specifico è associato un valore
func(b=1, a=2)

# Per questo motivo, se si volesse definire una funzione
# che genericamente accetta sia dei parametri passati come posizione,
# sia parametri passati come chiave, si può utilizzare gli operatori di unpacking
# per raccogliere tutti i valori passati alla funzione
def func (*args, **kwargs):
  print(*args)
  print({**kwargs})
# in questo modo, la funzione accetta qualsiasi tipo di argomento, sia posizionale, che tramite chiave


























