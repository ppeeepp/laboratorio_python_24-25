# DECORATORI
# = funzioni che chiamano funzioni
# -> chiamati tramite la @WrapperSyntax
# sono un metodo comodo per modificare il comportamento di una funzione
# in modo da estenderne le funzionalità, senza modificarla
def funzione_base() :
    print("Io sono la funzione base!")

# possiamo aggiungere operazioni prima di eseguire effettivamente funzione_base()
# funzione 'estensione': accetta come argomento la "funzione" da estendere
def estensione(funzione) :
    # contenitore
    def wrapper_della_funzione():
        # operazioni che "estendono la funzionalità"
        print("...aggiungo delle operazioni alla funzione...")
        # ritorna le funzione con le sue operazioni
        return funzione()
    # ritorno l'oggetto funzione contenitore
    return wrapper_della_funzione

# in questo modo possiamo usare la funzione originale:
funzione_base()         # Io sono la funzione base!
# oppure costruire un oggetto "funzione estesa"
funzione_estesa = estensione(funzione_base)
# chiamata alla funzione estesa
funzione_estesa()       # ...aggiungo delle operazioni alla funzione...
                        # Io sono la funzione base!

# in python si può quindi semplificare la creazione di funzioni estese chiamando un DECORATORE
# PRIMA: si definisce la funzione estensione:
# funzione 'estensione': accetta come argomento la "funzione" da estendere
def estensione(funzione) :
    # contenitore
    def wrapper_della_funzione():
        # operazioni che "estendono la funzionalità"
        print("...aggiungo delle operazioni alla funzione...")

        # ritorna le funzione con le sue operazioni
        return funzione()

    # ritorno l'oggetto funzione contenitore
    return wrapper_della_funzione
# POI: si costruisce la funzione da estendere, applicando il decoratore
@estensione
def funzione_base() :
    print("Io sono la funzione base!")
funzione_base()             # ...aggiungo delle operazioni alla funzione...
                            # Io sono la funzione base!

# scopo del decoratore: dedicarsi solo alla struttura della "funzione base",
# senza preoccuparsi delle operazioni in più necessarie per avere la funzione estesaù

# FUNZIONI CON ARGOMENTI
# E’ possibile applicare un decoratore anche a funzioni che hanno degli argomenti
# inoltrando tutti i parametri posizionali e con keyword utilizzando gli operatori di unpacking

# funzione decoratore
def metti_titolo(funzione):
    # la funzione contenitore deve fare l'unpacking di tutta la lista argomenti per posizione e per keyword
    def wrapper_della_funzione(*args, **kwargs):
        # nuova funzionalità
        print("L'operazione ha risultato:")
        # funzione originale
        return funzione(*args, **kwargs)
    # ritorna oggetto funzione
    return wrapper_della_funzione
# per poi definire normalmente una funzione con argomenti applicando il decoratore metti_titolo
# -> scrivo una normale funzione per fare la somma ma aggiungo il decoratore
@metti_titolo
def somma_numeri(a,b):
    print (a + b)

# e posso utilizzarla normalmente
# sia con argomenti posizionali:
somma_numeri(2, 4)
# sia con argomenti usati come keyword:
somma_numeri(a=2, b=3)
















