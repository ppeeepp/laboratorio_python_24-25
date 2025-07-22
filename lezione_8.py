# OOP
# OGGETTI: definiti tramite una classe che descrive il "progetto" di come è fatto, cosa contiene e come funzionerà l'oggetto che stiamo costruendo
# SINTASSI: keyword class + Nome in formato CapitalLetters + ":"
class MioOggetto:
    """docstring per descrivere l'oggetto"""
    #< statement >
    #...
    #< statement >
# fine della descrizione rientrando dal blocco

# Gli oggetti di una classe supportano due tipi di operazioni:
# 1. istanziare un oggetto
# 2. referenziare gli attributi
class Punto:
    """rappresenta un punto sul piano"""
    x = 3
    y = 4
# istanziare uno o più oggetti
p1 = Punto()
p2 = Punto()
# referenziare gli attributi di un oggetto - si usa la dot notation
p1.x = 7
p2.y = 5
# una particolarità degli oggetti è che i metodi di un oggetto possono solo modificare i propri data field
# -> si usa la keyword self (in altri linguaggi è this)

# inizializzazione -> metodo __init__ = metodo di inizializzazione
# -> è chiamato automaticamente quando si crea una nuova istanza di un oggetto
# ad esempio, è possibile assegnare il valore iniziale agli attributi dell'oggetto
class Punto:
    """Una classe per rappresentare e operere con una coppia di coordinate x, y come punto su un piano"""
    def __init__(self):
        """metodo della classe che inizializza la nuova istanza"""
        self.x = 0
        self.y = 0
p = Punto() # ho creato un oggetto punto con (0,0)
# inizializzazione con parametri
pp = Punto()
pp.x = 7
pp.y = 6
# ma si può modificare il metodo __init__ per rendere la classe molto più versatile
class Punto:
    """Una classe per rappresentare e operere con una coppia di coordinate x, y come punto su un piano"""
    def __init__(self, x, y):
        """Inizializza le coordinate del punto"""
        self.x = x
        self.y = y
# ora posso creare un oggetto Punto così:
punto = Punto(8,4)
# la funzione Punto() si chiama COSTRUTTORE

# METODI = azioni che l'oggetto può intraprendere per interagire con l'esterno
# si suddivisono in 3 categorie:
# 1 - metodi di istanza: sono applicati alla specifica istanza della classe (es. raffaello.forward() )
class Punto:
    """Una classe per rappresentare e operere con una coppia di coordinate x, y"""
    def __init__(self, x=0, y=0):
        """Inizializza le coordinate del punto"""
        self.x = x
        self.y = y
    def distanza_da_origine(self):
        """Calcola la distanza dall'origine"""
        distanza = (self.x ** 2 + self.y ** 2) ** 0.5
        return distanza
# 2 - metodi della classe: possono accedere liberamente ai metodi e attributi dell'oggetto per modificarne lo stato
# si riconoscono perchè utilizzano il parametro self e si possono utilizzare solo dopo che un oggetto è stato istanziato
# 2.1 classmethods: metodi comuni agli altri oggetti dello stesso tipo, appartengono alla classe e agiscono sulla classe stessa
#                   si aggiunge il decoratore @classmethod e si usa i parametro cls
class Punto:
    """Una classe per rappresentare e operere con una coppia di coordinate x, y"""
    @classmethod
    def origin(cls):
        """Metodo della classe che imposta i valori x=0, y=0"""
        return cls(0, 0)  # cls contiene tutte le informazioni sulla classe
    def __init__(self, x, y):
        """Inizializza le coordinate del punto"""
        self.x = x
        self.y = y
# 3 - metodi statici: non sono legati nè all'istanza, nè alla classe
# -> non possono modificare nè lo stato dell'oggeto nè della classe
# si costruiscono come funzioni a cui si aggiunge il decoratore @staticmethod e nessun primo parametro obbligatorio
class Punto:
    """Una classe per rappresentare e operere con una coppia di coordinate x, y"""
    @classmethod
    def origin(cls):
        """Metodo della classe che imposta i valori x=0, y=0"""
        return cls(0, 0)  # cls contiene tutte le informazioni sulla classe
    def __init__(self, x, y):
        """Inizializza le coordinate del punto"""
        self.x = x
        self.y = y
    @staticmethod
    def coordinata_valida(x):  # NON c'è self: non so nulla dell'istanza
        """controllo se la coordinata è entro il limite 100"""
        return x < 100
# METODI SPECIALI - non sono chiamati esplicitamente dal programmatore
# ma direttamente dall'interprete in casi particolari.
# Se il loro comportamento di default non è adatto allaa classe che stiamo descrivendo,
# va fatto l'overloading = si riscrivono
'''
__init__() :    chiamato nell’inizializzazione mc = MyClass()
 __str__() :    chiamato nella conversione a string o nel print str(mc)
__call__():     chiamato quando si usa un’istanza come una funzione mc()
__len__():      chiamato quando si usa il built-in len len(mc)
__contains__(x): chiamato quando si usa il built-in in x in mc
__getitem__(key): chiamato quando si usa l’operatore indicizzazione mc[key]
 __setitem__(key,val): chiamato quando si usa l’operatore indicizzazione mc[key] = val
'''
# EREDITARIETÀ - una classe può ereditare funzionalità da altre classi
# ci permette di definire classi che sono una specializzazione di un'altra classe già esistente
class PuntoMassa(Punto):
    """Una classe per rappresentare una massa puntiforme"""
    pass    # non fa niente
pm = PuntoMassa(4, 8)   # eredita tutti i metodi di Punto
class PuntoMassa(Punto):
    """Una classe per rappresentare una massa puntiforme"""
    def __init__(self, x=0, y=0, m=0):
        """Sovrascrive l'__init__ di Punto per tenere conto della massa"""
        Punto.__init__(self, x, y)  # Per le coordinate, uso l'__init__ di 'Punto'
        self.m = m            # Aggiungo il nuovo attributo: massa
    # e ci posso aggiungere altri metodi che "specializzano" questa classe
    g = 9.81
    def peso(self):
        """Restitusce il peso dell'oggetto"""
        return self.m * self.g

# cosa succede se i metodi hanno lo stesso nome?
class MyClass:
    def stampa(self):
        print('1 - La classe base è MyClass')

class MyChildClass(MyClass):
    def stampa(self):
        print('1 - La classe derivata è MyChildClass')

oggetto = MyChildClass()
oggetto.stampa()

# La funzione built-in super() ci aiuta: permette di accedere ai metodi delle classi parent
# -> evita di doversi ricordare il nome della classe base in modo esplicito
# -> semplifica la gestione di ereditarietà multipla
class MyClass:
    def stampa(self):
        print('2 - La classe base è MyClass')

class MyChildClass(MyClass):
    def stampa(self):
        print('2 - La classe derivata è MyChildClass')
        super().stampa()
oggetto = MyChildClass()
oggetto.stampa()

# regole base:
# il metodo della classe derivata è sempre chiamato prima di quello della classe base
# se ci sono più classi parent, il metodo è chiamato con l' ordine con cui sono elencate nella definizione della classe derivata
# -> MRO = METHOD RESOLUTION ORDER:  ordine con cui i metodi sono chiamati in caso di ereditarietà multiple
class A:
    def __init__(self):
        print('A init')

class B:
    def __init__(self):
        print('B init')

class C1(A,B):
    def __init__(self):
        print('C1 init')
        super().__init__()

class C2(B,A):
    def __init__(self):
        print('C2 init')
        super().__init__()

c1 = C1()   # A viene prima di B
c2 = C2()   # B viene prima di A
# EREDITARIETÀ MULTIPLA
class A:
    def __init__(self):
        print('A init')

class B(A):
    def __init__(self):
        print('B init')
        super().__init__()

class C(A):
    def __init__(self):
        print('C init')
        super().__init__()

class D1(C,B,A):
    def __init__(self):
        print('D1 init')
        super().__init__()

# super() si occupa per noi di risolvere le dipendenze, sempre seguendo l’MRO
# super(type, instance) accetta 2 parametri:
# il tipo da cui cominciare a cercare nell’MRO,
# e l’istanza (self) su cui applicare il metodo trovato.
# Se non specifico nulla, la funzione super() segue semplicemente l’ordine nell’MRO,
# ma se specifichiamo il tipo, super() cercherà nell’MRO il primo metodo adatto dopo il tipo richiesto

# CONVENZIONI
'''
- Per i nomi delle classi si usa il CapitalLetters: MyClass
- Per i nomi dei metodi si usa il snake_case: mc.my_method
- Mettere sempre una docstring che spieghi l’oggetto rappresentato da quella classe
- self per gli instance method
- cls per i class method
- Python non differenzia tra variabili pubbliche e private:
- metodi e attributi “privati” si indicano con under_score: mc._metodo_privato
'''





